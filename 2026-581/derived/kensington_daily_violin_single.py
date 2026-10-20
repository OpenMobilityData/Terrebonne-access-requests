#!/usr/bin/env python3
"""Single-season violin plots of DAILY bicycle counts at the Terrebonne/Kensington counter, each on its own axis.

Two figures per language: winter alone (December 1, 2025 to March 31, 2026, 121 days) and the rest of the counter's
first year alone (the other 244 days, July 26, 2025 to July 25, 2026). Same drawing as kensington_daily_violin.py
(density mirrored, every day a point, median bar, middle-half box), but the y-axis is fitted to the season shown, so
each distribution's own shape is legible. The rest-of-year axis stops at 1,100 (June 7, 2026, 3,035, a counter-fault
value, is noted). Source: kensington_daily_borough_release_2025-07_2026-08.csv in this folder (bundle 01, pp. 74-81).
Usage: python3 kensington_daily_violin_single.py [--csv=path] [--out=dir]   (run in 2026-581/derived/)
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

TXT = {
 'en': dict(w=dict(title='Daily bicycle counts on rue de Terrebonne at Kensington: the winter days', label='December 1, 2025 to March 31, 2026\n{n} days', ymax=140, cut=' Lower bound for March: westbound channel degraded from March 2026.'),
            o=dict(title='Daily bicycle counts on rue de Terrebonne at Kensington: the rest of the year', label='The other 244 days of the first year\n(July 26, 2025 to July 25, 2026, outside December–March)', ymax=1100,
                   cut=' Axis cut at 1,100: one day lies above it, June 7, 2026 (3,035, a counter-fault value). Lower bound: three outage days (May 29–31, 2026); westbound channel degraded from March 2026.'),
            sub='Distribution of the counter\'s daily totals (both directions); every day is a point;\nbar = median, box = middle half of days',
            ylab='bicycle passages per day', stat='median {med:.0f}\nmean {mean:.0f}\nmiddle half {q1:.0f}–{q3:.0f}\nmin {mn}, max {mx}',
            foot='Source: daily table released by the borough of Côte-des-Neiges–Notre-Dame-de-Grâce under access request 2026-581 (bundle 01, pp. 74–81).{cut}'),
 'fr': dict(w=dict(title='Comptages quotidiens de vélos, rue de Terrebonne à Kensington : les jours d’hiver', label='1er décembre 2025 au 31 mars 2026\n{n} jours', ymax=140, cut=' Borne inférieure en mars : canal ouest dégradé à partir de mars 2026.'),
            o=dict(title='Comptages quotidiens de vélos, rue de Terrebonne à Kensington : le reste de l’année', label='Les 244 autres jours de la première année\n(26 juillet 2025 au 25 juillet 2026, hors décembre–mars)', ymax=1100,
                   cut=' Axe coupé à 1 100 : un jour se trouve au-dessus, le 7 juin 2026 (3 035, valeur de compteur défaillant).'),
            sub='Distribution des totaux quotidiens du compteur (deux directions) ; chaque jour est un point ;\nbarre = médiane, boîte = moitié centrale des jours',
            ylab='passages de vélos par jour', stat='médiane {med:.0f}\nmoyenne {mean:.0f}\nmoitié centrale {q1:.0f}–{q3:.0f}\nmin {mn}, max {mx}',
            foot='Source : tableau quotidien communiqué par l’arrondissement de Côte-des-Neiges–Notre-Dame-de-Grâce (demande d’accès 2026-581, liasse 01, p. 74–81).{cut}'),
}

def main(argv):
    opts = dict(a[2:].split('=', 1) for a in argv if a.startswith('--'))
    path = opts.get('csv', CSV); out = opts.get('out', HERE)
    rows = [(dt.date.fromisoformat(r['date']), int(r['bike'] or 0)) for r in csv.DictReader(open(path, encoding='utf-8-sig'))]
    year = [(d, b) for d, b in rows if Y0 <= d <= Y1]
    data = {'w': [b for d, b in year if W0 <= d <= W1], 'o': [b for d, b in year if not (W0 <= d <= W1)]}
    rng = random.Random(1)
    for lang, T in TXT.items():
        for key, col in (('w', WINTER), ('o', OTHER)):
            S = T[key]; v = data[key]; vplot = [b for b in v if b <= S['ymax']]
            fig, ax = plt.subplots(figsize=(7.2, 6.4), dpi=150)
            parts = ax.violinplot([vplot], positions=[0], widths=0.8, showextrema=False, showmedians=False, points=400, bw_method=0.15)
            for body in parts['bodies']:
                body.set_facecolor(col); body.set_edgecolor(col); body.set_alpha(0.22); body.set_linewidth(1)
            ax.scatter([rng.uniform(-0.16, 0.16) for _ in vplot], vplot, s=11, color=col, alpha=0.55, linewidths=0, zorder=3)
            q1, med, q3 = statistics.quantiles(v, n=4)
            ax.add_patch(plt.Rectangle((-0.045, q1), 0.09, q3 - q1, facecolor=col, edgecolor='none', alpha=0.9, zorder=4))
            ax.plot([-0.11, 0.11], [med, med], color='#fcfcfb', linewidth=2.6, zorder=5); ax.plot([-0.11, 0.11], [med, med], color=INK, linewidth=1.4, zorder=6)
            mx = f'{max(v):,}' if lang == 'en' else f'{max(v):,}'.replace(',', ' ')
            ax.text(0.5, med, T['stat'].format(med=med, mean=sum(v) / len(v), q1=q1, q3=q3, mn=min(v), mx=mx), fontsize=10, color=INK, va='center', ha='left', linespacing=1.4)
            ax.set_xticks([0]); ax.set_xticklabels([S['label'].format(n=len(v))], fontsize=10, color=INK)
            ax.set_xlim(-0.6, 1.1); ax.set_ylim(0, S['ymax']); ax.set_ylabel(T['ylab'], fontsize=10, color=MUTED)
            if lang == 'fr':
                ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, p: f'{int(y):,}'.replace(',', ' ')))
            for s in ('top', 'right'): ax.spines[s].set_visible(False)
            ax.spines['left'].set_color('#c9cdd2'); ax.spines['bottom'].set_color('#c9cdd2')
            ax.yaxis.grid(True, color='#e2e4e1', linewidth=0.8, zorder=0); ax.set_axisbelow(True); ax.tick_params(colors=MUTED, length=0)
            fig.suptitle(S['title'], x=0.08, ha='left', fontsize=10.5, fontweight='bold', color=INK, y=0.985)
            ax.set_title(T['sub'], loc='left', fontsize=8.4, color=MUTED, pad=10)
            fig.text(0.08, 0.012, T['foot'].format(cut=S['cut']), fontsize=7.2, color=MUTED, wrap=True)
            fig.subplots_adjust(left=0.12, right=0.96, top=0.85, bottom=0.19)
            name = 'winter' if key == 'w' else 'rest'
            for ext in ('png', 'svg'):
                p = os.path.join(out, f'kensington_daily_violin_{name}_{lang}.{ext}'); fig.savefig(p); print('written', p)
            plt.close(fig)

if __name__ == '__main__':
    main(sys.argv[1:])
