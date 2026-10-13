#!/usr/bin/env python3
"""Reproduce the tables and figure of "Winter cycling on rue de Terrebonne and
the days snow is loaded" (access request 2026-300).

Inputs (paths relative to this script's folder unless given):
  ../raw/26072025_11052026.xlsx           hourly counter record by direction (request 2026-300)
  en_climate_daily_QC_7025251_2025_P1D.csv, ..._2026_P1D.csv   ECCC daily, Montréal-Trudeau
  loading_daily.csv                       City snow-removal loads by season/day/borough/sector
                                          (built from the transactions dataset; see README)
Outputs (written beside the script):
  kensington_daily_directional.csv, kensington_weather_loading_daily_2025-12_2026-03.csv,
  exposure_tables.txt, exposure_winter_2025-26.pdf / .png

Usage: python3 exposure_analysis.py [--workbook PATH] [--eccc-dir DIR] [--loading PATH]
"""
import argparse, os, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
SEASON = ('2025-12-01', '2026-03-31')
FIRM = ('2025-12-01', '2026-02-28')


def read_counter(path):
    import openpyxl
    ws = openpyxl.load_workbook(path, read_only=True).worksheets[0]
    rows = list(ws.iter_rows(min_row=4, values_only=True))
    d = pd.DataFrame(rows, columns=['t', 'bike', 'eb', 'wb', 'motor']).dropna(subset=['t'])
    d['t'] = pd.to_datetime(d['t'])
    day = d.groupby(d['t'].dt.date)[['bike', 'eb', 'wb', 'motor']].sum()
    day.index = pd.to_datetime(day.index); day.index.name = 'date'
    return day


def read_eccc(files):
    w = pd.concat([pd.read_csv(f, encoding='utf-8-sig') for f in files])
    w['date'] = pd.to_datetime(w['Date/Time'])
    w = w.set_index('date').rename(columns={'Total Snow (cm)': 'snow', 'Snow on Grnd (cm)': 'sog',
                                            'Total Precip (mm)': 'precip', 'Mean Temp (°C)': 'tmean'})
    return w[['snow', 'sog', 'precip', 'tmean']]


def runs(days):
    out, start, prev = [], None, None
    for d in days:
        if prev is None or (d - prev).days > 1:
            if start is not None: out.append((start, prev))
            start = d
        prev = d
    if start is not None: out.append((start, prev))
    return ', '.join(f'{a:%b %d}–{b:%b %d}' if a != b else f'{a:%b %d}' for a, b in out)


def window(mask, after):
    m = mask.values.copy()
    for i in np.where(m)[0]: m[i:i + 1 + after] = True
    return pd.Series(m, index=mask.index)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workbook', default=os.path.join(HERE, '..', 'raw', '26072025_11052026.xlsx'))
    ap.add_argument('--eccc-dir', default=HERE)
    ap.add_argument('--loading', default=os.path.join(HERE, 'loading_daily.csv'))
    a = ap.parse_args()

    day = read_counter(a.workbook)
    day.to_csv(os.path.join(HERE, 'kensington_daily_directional.csv'))
    w = read_eccc([os.path.join(a.eccc_dir, f'en_climate_daily_QC_7025251_{y}_P1D.csv') for y in (2025, 2026)])
    L = pd.read_csv(a.loading, parse_dates=['day'])
    cdn = L[L['ArrondissementCode'] == 'CDN']
    cur = cdn[cdn['season'] == '2025-2026']
    s = day.join(w, how='left')[SEASON[0]:SEASON[1]].copy()
    s['snow'] = s['snow'].fillna(0)
    s['loads_cdn'] = cur.groupby('day')['loads'].sum().reindex(s.index).fillna(0)
    s['loads_301'] = cur[cur['NomSecteur'].str.startswith('CDN-301')].groupby('day')['loads'].sum().reindex(s.index).fillna(0)
    s.to_csv(os.path.join(HERE, 'kensington_weather_loading_daily_2025-12_2026-03.csv'))

    out = []
    def P(*x): out.append(' '.join(str(v) for v in x))

    def table(w, label):
        EB = w['eb'].sum()
        P(f'\n== {label}: {len(w)} days, eastbound {int(EB)}, westbound {int(w["wb"].sum())}, total {int(w["bike"].sum())}')
        def trigger(load_mask):
            t = load_mask.values.copy()
            for i in np.where(t)[0]:
                for k in range(1, 4):
                    if i - k >= 0 and w['snow'].iloc[i - k] >= 2.5: t[i - k:i] = True
            return pd.Series(t, index=w.index)
        trig = trigger(w['loads_cdn'] >= 100)
        trig301 = trigger(w['loads_301'] >= 40)
        rules = [
            ('Borough loading days (>=100 loads)', w['loads_cdn'] >= 100),
            ('Sector CDN-301 loading days (>=40 loads)', w['loads_301'] >= 40),
            ('From triggering snowfall (>=2.5 cm) through loading', trig),
            ('From triggering snowfall through CDN-301 loading', trig301),
            ('Any day with loading activity in the borough', w['loads_cdn'] >= 1),
            ('Any day with loading activity in CDN-301', w['loads_301'] >= 1),
            ('Any day with >=2.5 cm of snow', w['snow'] >= 2.5),
            ('>=2.5 cm day and the day after', window(w['snow'] >= 2.5, 1)),
            ('>=5 cm day and four days after', window(w['snow'] >= 5, 4)),
            ('Any day with measurable snow', w['snow'] > 0),
            ('Zero-snow days', w['snow'] == 0),
        ]
        for name, mk in rules:
            P(f'  {name:55s} days {int(mk.sum()):3d}  EB {int(w["eb"][mk].sum()):5d}  {w["eb"][mk].sum() / EB:4.0%}')
        P(f'  loading episodes (borough): {runs(w.index[w["loads_cdn"] >= 100])}')
        P(f'  loading episodes (CDN-301): {runs(w.index[w["loads_301"] >= 40])}')
        P(f'  mean EB/day: dry {w["eb"][w["snow"] == 0].mean():.1f}, trace {w["eb"][(w["snow"] > 0) & (w["snow"] < 2.5)].mean():.1f}, '
          f'>=2.5 cm {w["eb"][w["snow"] >= 2.5].mean():.1f}; loading days {w["eb"][w["loads_cdn"] >= 100].mean():.1f}, other {w["eb"][w["loads_cdn"] < 100].mean():.1f}')
        P(f'  corr(EB, snow) {w["eb"].corr(w["snow"]):+.2f}; corr(EB, snow on ground) {w["eb"].corr(w["sog"]):+.2f}; corr(EB, mean temp) {w["eb"].corr(w["tmean"]):+.2f}')

    table(s, 'Season Dec 1 - Mar 31')
    table(s[FIRM[0]:FIRM[1]], 'Firm window Dec 1 - Feb 28')

    P('\n== 2025-26 counts under each season\'s CDN loading calendar (>=100 loads/day)')
    EB = s['eb'].sum()
    for sea, g in cdn.groupby('season'):
        y0 = int(sea[:4]); days = []
        for d, n in zip(g.groupby('day')['loads'].sum().index, g.groupby('day')['loads'].sum()):
            if n < 100: continue
            try: dd = pd.Timestamp(year=2025 + (d.year - y0), month=d.month, day=d.day)
            except ValueError: continue
            if pd.Timestamp(SEASON[0]) <= dd <= pd.Timestamp(SEASON[1]): days.append(dd)
        mk = s.index.isin(days)
        P(f'  {sea}: {int(mk.sum()):3d} loading days -> EB {int(s["eb"][mk].sum()):4d} ({s["eb"][mk].sum() / EB:.0%})')

    P('\n== Season context (city-wide m3 hauled)')
    for sea, g in L.groupby('season'): P(f'  {sea}: {g["m3"].sum() / 1e6:5.2f} M m3')

    P('\n== Counter direction balance by month (eastbound share)')
    mo = day.groupby(day.index.to_period('M'))[['eb', 'wb']].sum()
    for p, r in mo.iterrows(): P(f'  {p}: EB {int(r.eb):6d}  WB {int(r.wb):6d}  {r.eb / (r.eb + r.wb):.0%}')

    txt = '\n'.join(out) + '\n'
    open(os.path.join(HERE, 'exposure_tables.txt'), 'w').write(txt); print(txt)

    # figure
    import matplotlib; matplotlib.use('Agg')
    import matplotlib.pyplot as plt, matplotlib.dates as md
    blue, grey, ink, sub = '#2a78d6', '#c3c2b7', '#0b0b0b', '#52514e'
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.2, 4.2), sharex=True, gridspec_kw=dict(height_ratios=[3, 1.2], hspace=0.12))
    snowday = s['snow'] >= 2.5
    a1.bar(s.index[~snowday], s['eb'][~snowday], width=0.8, color=blue, linewidth=0, label='dry or trace day (<2.5 cm)')
    a1.bar(s.index[snowday], s['eb'][snowday], width=0.8, color=grey, linewidth=0, label='snow day (≥2.5 cm)')
    a1.set_ylabel('Eastbound trips / day', color=sub, fontsize=8); a1.legend(frameon=False, fontsize=7.5, loc='upper left')
    a2.bar(s.index, s['snow'], width=0.8, color=sub, linewidth=0); a2.set_ylabel('Snowfall, cm', color=sub, fontsize=8)
    for a in (a1, a2):
        a.spines[['top', 'right']].set_visible(False); a.spines[['left', 'bottom']].set_color(grey)
        a.tick_params(colors=sub, labelsize=7.5); a.grid(axis='y', color='#eeeeea', linewidth=0.6); a.set_axisbelow(True)
    a2.xaxis.set_major_locator(md.MonthLocator()); a2.xaxis.set_major_formatter(md.DateFormatter('%b %Y'))
    fig.suptitle('Terrebonne at Kensington, eastbound bicycle trips and snowfall, Dec 1 2025 – Mar 31 2026', fontsize=9, color=ink, x=0.01, ha='left')
    fig.text(0.01, 0.005, 'Counter: access request 2026-300 (eastbound). Snowfall: Environment Canada, Montréal–Trudeau Intl A, daily.', fontsize=6.5, color=sub)
    for ext in ('pdf', 'png'):
        fig.savefig(os.path.join(HERE, f'exposure_winter_2025-26.{ext}'), bbox_inches='tight', dpi=160)


if __name__ == '__main__':
    main()
