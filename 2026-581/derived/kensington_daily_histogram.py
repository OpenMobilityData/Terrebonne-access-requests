#!/usr/bin/env python3
"""Histograms of DAILY bicycle counts at the Terrebonne/Kensington counter: winter days against non-winter days.

Each series is the distribution of the counter's daily totals over the days of one season, drawn as a frequency
polygon (a thin line through the bin values, not stepped bars). Winter = December 1, 2025 to March 31, 2026
(121 days); non-winter = the other 244 days of the counter's first year (July 26, 2025 to July 25, 2026).
Two versions: absolute (days per bin) and normalized (share of the season's days per bin; each line sums to one).
Source: kensington_daily_borough_release_2025-07_2026-08.csv in this folder (bundle 01, pp. 74-81).
Usage: python3 kensington_daily_histogram.py [--csv=path] [--out=dir] [--bin=25] [--xmax=1050]   (run in 2026-581/derived/)
"""
import csv, datetime as dt, os, sys, statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, 'kensington_daily_borough_release_2025-07_2026-08.csv')
Y0, Y1 = dt.date(2025, 7, 26), dt.date(2026, 7, 25)
W0, W1 = dt.date(2025, 12, 1), dt.date(2026, 3, 31)
WINTER, OTHER, INK, MUTED = '#2a78d6', '#eb6834', '#1f2428', '#5f6b74'

TXT = {
 'en': dict(title={'abs': 'Daily bicycle counts on rue de Terrebonne at Kensington: winter days and the rest of the year',
                   'rel': 'Daily bicycle counts on rue de Terrebonne at Kensington: winter days and the rest of the year'},
            sub={'abs': 'Distribution of the counter\'s daily totals (both directions), bins of {b} passages a day; first year of operation, July 26, 2025 to July 25, 2026',
                 'rel': 'Normalized: each line is the share of its own season\'s days per bin and sums to 100 %; bins of {b} passages a day; first year, July 26, 2025 to July 25, 2026'},
            xlab='bicycle passages per day', ylab={'abs': 'number of days', 'rel': 'share of the season\'s days'},
            w='December to March: {n} days, median {med:.0f} a day, mean {mean:.0f}', o='Rest of the year: {n} days, median {med:.0f} a day, mean {mean:.0f}',
            foot='Source: daily table released by the borough of Côte-des-Neiges–Notre-Dame-de-Grâce under access request 2026-581 (bundle 01, pp. 74–81). '
                 'Each point is the number of days (or their share) whose daily total fell in that bin, plotted at the bin centre. Lower bound: three outage days (May 29–31, 2026); westbound channel degraded from March 2026.'),
 'fr': dict(title={'abs': 'Comptages quotidiens de vélos sur la rue de Terrebonne à Kensington : jours d’hiver et reste de l’année',
                   'rel': 'Comptages quotidiens de vélos sur la rue de Terrebonne à Kensington : jours d’hiver et reste de l’année'},
            sub={'abs': 'Distribution des totaux quotidiens du compteur (deux directions), classes de {b} passages par jour ; première année de service, 26 juillet 2025 au 25 juillet 2026',
                 'rel': 'Normalisé : chaque courbe donne la part des jours de sa saison par classe et somme à 100\u202f% ; classes de {b} passages par jour ; première année, 26 juillet 2025 au 25 juillet 2026'},
            xlab='passages de vélos par jour', ylab={'abs': 'nombre de jours', 'rel': 'part des jours de la saison'},
            w='Décembre à mars : {n} jours, médiane {med:.0f} par jour, moyenne {mean:.0f}', o='Reste de l’année : {n} jours, médiane {med:.0f} par jour, moyenne {mean:.0f}',
            foot='Source : tableau quotidien communiqué par l’arrondissement de Côte-des-Neiges–Notre-Dame-de-Grâce (demande d’accès 2026-581, liasse 01, p. 74–81). '
                 'Chaque point donne le nombre de jours (ou leur part) dont le total quotidien tombe dans la classe, placé au centre de la classe. Borne inférieure : trois jours de panne (29–31 mai 2026) ; canal ouest dégradé à partir de mars 2026.'),
}

def main(argv):
    opts = dict(a[2:].split('=', 1) for a in argv if a.startswith('--'))
    path = opts.get('csv', CSV); out = opts.get('out', HERE); B = int(opts.get('bin', 25))
    rows = [(dt.date.fromisoformat(r['date']), int(r['bike'] or 0)) for r in csv.DictReader(open(path, encoding='utf-8-sig'))]
    year = [(d, b) for d, b in rows if Y0 <= d <= Y1]
    winter = [b for d, b in year if W0 <= d <= W1]; other = [b for d, b in year if not (W0 <= d <= W1)]
    top = int(opts.get('xmax', 1050))          # last bin is open-ended; values above it are folded in (see footer)
    edges = list(range(0, top + B, B)); centres = [e + B / 2 for e in edges[:-1]]
    above = [(d, b) for d, b in year if b >= top]
    def hist(v):
        h = [0] * (len(edges) - 1)
        for x in v:
            h[min(x // B, len(h) - 1)] += 1
        return h
    hw, ho = hist(winter), hist(other)
    print('winter', len(winter), 'median', statistics.median(winter), 'mean', round(sum(winter) / len(winter), 1), 'max', max(winter))
    print('other ', len(other), 'median', statistics.median(other), 'mean', round(sum(other) / len(other), 1), 'max', max(other))
    print('bins', B, 'winter days per bin', hw[:8], '... other', ho[:12])
    for lang, T in TXT.items():
        for kind in ('abs', 'rel'):
            yw = hw if kind == 'abs' else [h / len(winter) for h in hw]
            yo = ho if kind == 'abs' else [h / len(other) for h in ho]
            fig, ax = plt.subplots(figsize=(11, 5.6), dpi=150)
            def trim(c, y):   # stop each line after its last non-empty bin (one zero kept), instead of a row of zero markers
                last = max(i for i, v in enumerate(y) if v) + 2
                return c[:last], y[:last]
            ax.plot(*trim(centres, yo), color=OTHER, linewidth=1.6, marker='o', markersize=4, zorder=2,
                    label=T['o'].format(n=len(other), med=statistics.median(other), mean=sum(other) / len(other)))
            ax.plot(*trim(centres, yw), color=WINTER, linewidth=1.6, marker='o', markersize=4, zorder=3,
                    label=T['w'].format(n=len(winter), med=statistics.median(winter), mean=sum(winter) / len(winter)))
            ax.set_xlim(0, top); ax.set_xticks(list(range(0, top + 1, 100)))
            ticks = list(range(0, top + 1, 100))
            ax.set_xticklabels([str(v) if v != ticks[-1] else f'{v}+' for v in ticks])
            ax.set_xlabel(T['xlab'], fontsize=10, color=MUTED); ax.set_ylabel(T['ylab'][kind], fontsize=10, color=MUTED)
            if kind == 'rel':
                ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0, symbol=' %' if lang == 'fr' else ' %'))
            for s in ('top', 'right'): ax.spines[s].set_visible(False)
            ax.spines['left'].set_color('#c9cdd2'); ax.spines['bottom'].set_color('#c9cdd2')
            ax.yaxis.grid(True, color='#e2e4e1', linewidth=0.8, zorder=1); ax.set_axisbelow(True); ax.tick_params(colors=MUTED, length=0)
            leg = ax.legend(frameon=False, fontsize=9.5, loc='upper right'); [t_.set_color(INK) for t_ in leg.get_texts()]
            fig.suptitle(T['title'][kind], x=0.06, ha='left', fontsize=12.5, fontweight='bold', color=INK, y=0.985)
            ax.set_title(T['sub'][kind].format(b=B), loc='left', fontsize=9.2, color=MUTED, pad=10)
            foot = T['foot']
            if above:
                foot += (' The last bin also holds ' if lang == 'en' else ' La dernière classe contient aussi ') + '; '.join(
                    (f'{d.strftime("%B %-d, %Y")} ({b:,}, a counter-fault value)' if lang == 'en' else f'le {d.day} {["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"][d.month]} {d.year} ({b:,}, valeur de compteur défaillant)'.replace(',', '\u202f')) for d, b in above) + '.'
            fig.text(0.06, 0.012, foot, fontsize=7.6, color=MUTED, wrap=True)
            fig.subplots_adjust(left=0.08, right=0.98, top=0.86, bottom=0.2)
            for ext in ('png', 'svg'):
                p = os.path.join(out, f'kensington_daily_histogram_{kind}_{lang}.{ext}'); fig.savefig(p); print('written', p)
            plt.close(fig)

if __name__ == '__main__':
    main(sys.argv[1:])
