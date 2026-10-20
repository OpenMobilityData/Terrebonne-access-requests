#!/usr/bin/env python3
"""Violin plot of DAILY bicycle counts at the Terrebonne/Kensington counter: winter days beside the rest of the year.

Each violin is the distribution of the counter's daily totals over the days of one season (kernel density, mirrored),
with every day drawn as a point, the median as a bar and the quartiles as a box. Winter = December 1, 2025 to
March 31, 2026 (121 days); rest of the year = the other 244 days of the counter's first year (July 26, 2025 to
July 25, 2026). The y-axis stops at 1,100; the one day above it (June 7, 2026, 3,035, a counter-fault value) is noted.
Source: kensington_daily_borough_release_2025-07_2026-08.csv in this folder (bundle 01, pp. 74-81).
Usage: python3 kensington_daily_violin.py [--csv=path] [--out=dir]   (run in 2026-581/derived/)
"""
import csv, datetime as dt, os, sys, statistics, random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, 'kensington_daily_borough_release_2025-07_2026-08.csv')
Y0, Y1 = dt.date(2025, 7, 26), dt.date(2026, 7, 25)
W0, W1 = dt.date(2025, 12, 1), dt.date(2026, 3, 31)
WINTER, OTHER, INK, MUTED = '#2a78d6', '#eb6834', '#1f2428', '#5f6b74'
YMAX = 1100

TXT = {
 'en': dict(title='Daily bicycle counts on rue de Terrebonne at Kensington: winter and the rest of the year',
            sub='Each violin is the distribution of the counter\'s daily totals (both directions) over one season; every day is a point; bar = median, box = middle half. First year, July 26, 2025 to July 25, 2026',
            w='December to March\n{n} days', o='Rest of the year\n{n} days', ylab='bicycle passages per day',
            stat='median {med:.0f}\nmean {mean:.0f}\nmin {mn}, max {mx}',
            foot='Source: daily table released by the borough of Côte-des-Neiges–Notre-Dame-de-Grâce under access request 2026-581 (bundle 01, pp. 74–81). '
                 'Axis cut at {ymax:,}: one day lies above it, June 7, 2026 (3,035, a counter-fault value). Lower bound: three outage days (May 29–31, 2026); westbound channel degraded from March 2026.'),
 'fr': dict(title='Comptages quotidiens de vélos, rue de Terrebonne à Kensington : hiver et reste de l’année',
            sub='Chaque violon est la distribution des totaux quotidiens du compteur (deux directions) sur une saison ; chaque jour est un point ; barre = médiane, boîte = moitié centrale. Première année, 26 juillet 2025 au 25 juillet 2026',
            w='Décembre à mars\n{n} jours', o='Reste de l’année\n{n} jours', ylab='passages de vélos par jour',
            stat='médiane {med:.0f}\nmoyenne {mean:.0f}\nmin {mn}, max {mx}',
            foot='Source : tableau quotidien communiqué par l’arrondissement de Côte-des-Neiges–Notre-Dame-de-Grâce (demande d’accès 2026-581, liasse 01, p. 74–81). '
                 'Axe coupé à {ymax} : un jour se trouve au-dessus, le 7 juin 2026 (3 035, valeur de compteur défaillant). Borne inférieure : trois jours de panne (29–31 mai 2026) ; canal ouest dégradé à partir de mars 2026.'),
}

def main(argv):
    opts = dict(a[2:].split('=', 1) for a in argv if a.startswith('--'))
    path = opts.get('csv', CSV); out = opts.get('out', HERE)
    rows = [(dt.date.fromisoformat(r['date']), int(r['bike'] or 0)) for r in csv.DictReader(open(path, encoding='utf-8-sig'))]
    year = [(d, b) for d, b in rows if Y0 <= d <= Y1]
    winter = [b for d, b in year if W0 <= d <= W1]; other = [b for d, b in year if not (W0 <= d <= W1)]
    other_plot = [b for b in other if b <= YMAX]          # the density is drawn without the counter-fault day; the point count still says 244
    rng = random.Random(1)
    for lang, T in TXT.items():
        fig, ax = plt.subplots(figsize=(9, 6.4), dpi=150)
        parts = ax.violinplot([winter, other_plot], positions=[0, 1], widths=0.8, showextrema=False, showmedians=False, points=400, bw_method=0.15)
        for body, col in zip(parts['bodies'], (WINTER, OTHER)):
            body.set_facecolor(col); body.set_edgecolor(col); body.set_alpha(0.22); body.set_linewidth(1)
        for i, (v, col) in enumerate(((winter, WINTER), (other_plot, OTHER))):
            xs = [i + rng.uniform(-0.16, 0.16) for _ in v]
            ax.scatter(xs, v, s=9, color=col, alpha=0.55, linewidths=0, zorder=3)
            q1, med, q3 = statistics.quantiles(v, n=4)
            ax.add_patch(plt.Rectangle((i - 0.045, q1), 0.09, q3 - q1, facecolor=col, edgecolor='none', alpha=0.9, zorder=4))
            ax.plot([i - 0.11, i + 0.11], [med, med], color='#fcfcfb', linewidth=2.6, zorder=5)
            ax.plot([i - 0.11, i + 0.11], [med, med], color=INK, linewidth=1.4, zorder=6)
        full = ((winter, 'w'), (other, 'o'))
        for i, (v, key) in enumerate(full):
            ax.text(i + 0.46, statistics.median(v) + (40 if key == 'w' else 0), T['stat'].format(med=statistics.median(v), mean=sum(v) / len(v), mn=min(v), mx=(f'{max(v):,}' if lang == 'en' else f'{max(v):,}'.replace(',', ' '))),
                    fontsize=9.5, color=INK, va='center', ha='left', linespacing=1.35)
        ax.set_xticks([0, 1]); ax.set_xticklabels([T['w'].format(n=len(winter)), T['o'].format(n=len(other))], fontsize=10.5, color=INK)
        ax.set_xlim(-0.6, 1.9); ax.set_ylim(0, YMAX); ax.set_ylabel(T['ylab'], fontsize=10, color=MUTED)
        if lang == 'fr':
            ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f'{int(v):,}'.replace(',', ' ')))
        for s in ('top', 'right'): ax.spines[s].set_visible(False)
        ax.spines['left'].set_color('#c9cdd2'); ax.spines['bottom'].set_color('#c9cdd2')
        ax.yaxis.grid(True, color='#e2e4e1', linewidth=0.8, zorder=0); ax.set_axisbelow(True); ax.tick_params(colors=MUTED, length=0)
        fig.suptitle(T['title'], x=0.07, ha='left', fontsize=11.5, fontweight='bold', color=INK, y=0.985)
        ax.set_title(T['sub'], loc='left', fontsize=8.6, color=MUTED, pad=10, wrap=True)
        fig.text(0.07, 0.012, T['foot'].format(ymax=YMAX), fontsize=7.4, color=MUTED, wrap=True)
        fig.subplots_adjust(left=0.1, right=0.98, top=0.84, bottom=0.17)
        for ext in ('png', 'svg'):
            p = os.path.join(out, f'kensington_daily_violin_{lang}.{ext}'); fig.savefig(p); print('written', p)
        plt.close(fig)
    print('winter', len(winter), statistics.quantiles(winter, n=4), 'other', len(other), statistics.quantiles(other, n=4))

if __name__ == '__main__':
    main(sys.argv[1:])
