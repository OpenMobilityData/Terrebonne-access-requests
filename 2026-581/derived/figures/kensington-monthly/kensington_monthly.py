#!/usr/bin/env python3
"""Monthly histogram of bicycle passages at the Terrebonne/Kensington counter, first counter year.

Source: the borough's daily table released under access request 2026-581 (bundle 01, pp. 74-81), as the CSV
kensington_daily_borough_release_2025-07_2026-08.csv in 2026-581/derived/, two levels up.
Bars: mean bicycle passages per day in each calendar month, both directions, Aug 2025 - Jul 2026
(July 2026 = 1-25 only, the end of the counter's first year, July 26, 2025 - July 25, 2026).
The December-March band is the window the borough proposes to convert; its label gives the window's
passages, share of the year, and per-day rate. Counts, not opinions.
Usage: python3 kensington_monthly.py [--csv=path] [--out=dir]   (run in its own folder)
"""
import csv, datetime as dt, os, sys, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, '..', '..', 'kensington_daily_borough_release_2025-07_2026-08.csv')
Y0, Y1 = dt.date(2025, 7, 26), dt.date(2026, 7, 25)
W0, W1 = dt.date(2025, 12, 1), dt.date(2026, 3, 31)
BAR, BAND, INK, MUTED = '#2a78d6', '#e9ebee', '#1f2428', '#5f6b74'

TXT = {
 'en': dict(title='Bicycle passages per day on rue de Terrebonne at Kensington, by month',
            sub='Both directions, borough counter, first year of operation (July 26, 2025 to July 25, 2026); July 2026 = 1–25',
            band='December to March:\n{w} passages, {wpd:.0f} a day\n= {share:.1f} % of the year\'s {tot} passages',
            ylab='passages per day (monthly mean)',
            foot='Source: daily table released by the borough of Côte-des-Neiges–Notre-Dame-de-Grâce under access request 2026-581 (bundle 01, pp. 74–81). '
                 'Year total {tot} ({tpd:.0f} a day). Lower bound: three outage days (May 29–31, 2026); westbound channel degraded from March 2026.',
            months=['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']),
 'fr': dict(title='Passages de vélos par jour sur la rue de Terrebonne à Kensington, par mois',
            sub='Deux directions, compteur de l’arrondissement, première année de service (26 juillet 2025 au 25 juillet 2026) ; juillet 2026 = 1 au 25',
            band='Décembre à mars :\n{w} passages, {wpd:.0f} par jour\n= {share:.1f} % des {tot} passages de l’année',
            ylab='passages par jour (moyenne du mois)',
            foot='Source : tableau quotidien communiqué par l’arrondissement de Côte-des-Neiges–Notre-Dame-de-Grâce (demande d’accès 2026-581, liasse 01, p. 74–81). '
                 'Total de l’année {tot} ({tpd:.0f} par jour). Borne inférieure : trois jours de panne (29–31 mai 2026) ; canal ouest dégradé à partir de mars 2026.',
            months=['août', 'sept.', 'oct.', 'nov.', 'déc.', 'janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.']),
}

def fr_num(n):
    return f'{n:,}'.replace(',', ' ')

def main(argv):
    opts = dict(a[2:].split('=', 1) for a in argv if a.startswith('--'))
    path = opts.get('csv', CSV); out = opts.get('out', HERE)
    rows = [(dt.date.fromisoformat(r['date']), int(r['bike'] or 0)) for r in csv.DictReader(open(path, encoding='utf-8-sig'))]
    year = [(d, b) for d, b in rows if Y0 <= d <= Y1]
    tot = sum(b for _, b in year)
    bym = collections.defaultdict(lambda: [0, 0])
    for d, b in year:
        k = (d.year, d.month); bym[k][0] += 1; bym[k][1] += b
    keys = [(2025, m) for m in range(8, 13)] + [(2026, m) for m in range(1, 8)]
    pd_ = [bym[k][1] / bym[k][0] for k in keys]
    w = sum(b for d, b in year if W0 <= d <= W1); wdays = sum(1 for d, _ in year if W0 <= d <= W1)
    for lang, T in TXT.items():
        fig, ax = plt.subplots(figsize=(11, 5.6), dpi=150)
        x = range(len(keys))
        ax.axvspan(3.5, 7.5, color=BAND, zorder=0)
        bars = ax.bar(x, pd_, width=0.68, color=BAR, zorder=2)
        for i, v in enumerate(pd_):
            ax.text(i, v + 8, f'{v:.0f}', ha='center', va='bottom', fontsize=10, color=INK)
        num = (lambda n: fr_num(n)) if lang == 'fr' else (lambda n: f'{n:,}')
        band = T['band'].format(w=num(w), share=100 * w / tot, wpd=w / wdays, tot=num(tot))
        if lang == 'fr':
            band = band.replace(f'{100 * w / tot:.1f} %', f'{100 * w / tot:.1f}'.replace('.', ',') + '\u202f%')
        ax.text(5.5, max(pd_) * 0.93, band, ha='center', va='top', fontsize=10.5, color=INK, linespacing=1.4)
        ax.set_xticks(list(x)); ax.set_xticklabels([f'{T["months"][i]} {k[0]}' if i in (0, 5) else T['months'][i] for i, k in enumerate(keys)], fontsize=10)
        ax.set_ylabel(T['ylab'], fontsize=10, color=MUTED)
        ax.set_ylim(0, max(pd_) * 1.12)
        for s in ('top', 'right'): ax.spines[s].set_visible(False)
        ax.spines['left'].set_color('#c9cdd2'); ax.spines['bottom'].set_color('#c9cdd2')
        ax.yaxis.grid(True, color='#e2e4e1', linewidth=0.8, zorder=1); ax.set_axisbelow(True)
        ax.tick_params(colors=MUTED, length=0)
        fig.suptitle(T['title'], x=0.06, ha='left', fontsize=13.5, fontweight='bold', color=INK, y=0.985)
        ax.set_title(T['sub'], loc='left', fontsize=9.5, color=MUTED, pad=10)
        foot = T['foot'].format(tot=num(tot), tpd=tot / len(year))
        fig.text(0.06, 0.012, foot, fontsize=7.6, color=MUTED, wrap=True)
        fig.subplots_adjust(left=0.08, right=0.98, top=0.86, bottom=0.2)
        for ext in ('png', 'svg'):
            p = os.path.join(out, f'kensington_monthly_2025-26_{lang}.{ext}'); fig.savefig(p); print('written', p)
        plt.close(fig)
    print('year', tot, 'winter', w, f'{100*w/tot:.2f}%', [f'{v:.0f}' for v in pd_])

if __name__ == '__main__':
    main(sys.argv[1:])
