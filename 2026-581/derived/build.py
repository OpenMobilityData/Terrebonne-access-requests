#!/usr/bin/env python3
"""Stamp a version tag (YYYY-MM-DD-hh-mm-ss, America/Toronto) into the
derived documents, compile them, and regenerate the summary-point extracts
and text files.

Usage:  python3 build.py            # stamp now, build everything
        python3 build.py --no-stamp # rebuild without changing the tag

The tag lives in each .tex as  \\newcommand{\\docversion}{...}  and appears in
the page footer (small grey) and in the PDF metadata (Subject). The .txt
files carry it as a last line. One tag is shared by all files built in the
same run, so a set of files can be identified as belonging together.
"""
import re, subprocess, sys, unicodedata
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = '/home/claude/atip_summary'
SUMMARIES = {
    'en': 'Terrebonne_2026-581_executive_summary_en.tex',
    'fr': 'Terrebonne_2026-581_executive_summary_fr.tex',
}
EXTRACTS = {
    'en': 'Terrebonne_2026-581_summary_points_en.tex',
    'fr': 'Terrebonne_2026-581_summary_points_fr.tex',
}
TXT_HEAD = {
    'en': ["Access request 2026-581: what the borough's file shows",
           "Summary points of the executive summary. Full analysis, page references and the released documents: https://github.com/OpenMobilityData/Terrebonne-access-requests"],
    'fr': ["Demande d'accès 2026-581 : ce que révèle le dossier de l'arrondissement",
           "Points sommaires du sommaire et analyse. Analyse complète, références aux pages et documents communiqués : https://github.com/OpenMobilityData/Terrebonne-access-requests"],
}

def stamp(path, tag):
    s = open(path, encoding='utf-8').read()
    s2, n = re.subn(r'\\newcommand\{\\docversion\}\{[^}]*\}', r'\\newcommand{\\docversion}{%s}' % tag, s)
    assert n == 1, f'{path}: expected one \\docversion definition, found {n}'
    open(path, 'w', encoding='utf-8').write(s2)

def compile_tex(path):
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', path], cwd=HERE,
                           capture_output=True, text=True, errors='replace')
    out = r.stdout
    bad = [l for l in out.splitlines() if l.startswith('!') or 'Overfull' in l]
    pages = re.search(r'Output written on \S+ \((\d+) pages?', out)
    print(f'{path}: {pages.group(1) if pages else "?"} pages' + (f'  WARN {bad}' if bad else ''))

def extract(src_tex, dst_tex):
    src = open(src_tex, encoding='utf-8').read()
    a = src.index('\\begin{enumerate}[nosep]'); b = src.index('\\end{enumerate}', a) + len('\\end{enumerate}')
    d = open(dst_tex, encoding='utf-8').read()
    x = d.index('\\begin{enumerate}'); y = d.index('\\end{enumerate}') + len('\\end{enumerate}')
    opts = d[x:d.index(']', x) + 1]
    open(dst_tex, 'w', encoding='utf-8').write(d[:x] + src[a:b].replace('\\begin{enumerate}[nosep]', opts) + d[y:])

def detex(s):
    s = s.replace('{,}', ',').replace('\\,', ' ').replace('~', ' ')
    s = re.sub(r'\\ldots\\\s', ' … ', s); s = s.replace('\\ldots', '…')
    for pat, ch in [(r"\\'\{?e\}?", 'é'), (r"\\'\{?E\}?", 'É'), (r"\\`\{?e\}?", 'è'), (r"\\`\{?a\}?", 'à'),
                    (r"\\\^\{?o\}?", 'ô'), (r"\\\^\{?a\}?", 'â'), (r"\\\^\{?e\}?", 'ê'), (r"\\c\{c\}", 'ç')]:
        s = re.sub(pat, ch, s)
    s = s.replace('``', '“').replace("''", '”')
    s = re.sub(r'\\begin\{minipage\}\[t\]\{\\linewidth\}', '', s); s = re.sub(r'\\end\{minipage\}\\vspace\{[^}]*\}', '', s)
    s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s); s = re.sub(r'\\emph\{([^}]*)\}', r'\1', s)
    s = s.replace('$-95$ \\%', '−95 %').replace('$-95$\\%', '−95%').replace('\\$', '$').replace('\\%', '%').replace('--', '–')
    return re.sub(r'\s+', ' ', s).strip()

def build_txt(tex, out, head, tag, lang):
    src = open(tex, encoding='utf-8').read()
    a = src.index('\\begin{enumerate}'); b = src.index('\\end{enumerate}')
    items = [i.strip() for i in src[src.index(']', a) + 1:b].split('\\item') if i.strip()]
    lines = head + ['']
    for it in items: lines += [detex(it), '']
    lines.append(('Version ' if lang == 'en' else 'Version ') + tag)
    txt = '\n'.join(lines) + '\n'
    assert '{' not in txt and '\\' not in txt, re.findall(r'.{25}[{\\].{25}', txt)
    open(out, 'w', encoding='utf-8').write(txt)
    print(f'{out}: {len(items)} points, version {tag}')

def main():
    no_stamp = '--no-stamp' in sys.argv
    tag = datetime.now(ZoneInfo('America/Toronto')).strftime('%Y-%m-%d-%H-%M-%S')
    for lang in ('en', 'fr'):
        extract(f'{HERE}/{SUMMARIES[lang]}', f'{HERE}/{EXTRACTS[lang]}')
    files = list(SUMMARIES.values()) + list(EXTRACTS.values())
    if not no_stamp:
        for f in files: stamp(f'{HERE}/{f}', tag)
    else:
        tag = re.search(r'\\newcommand\{\\docversion\}\{([^}]*)\}', open(f'{HERE}/{SUMMARIES["en"]}', encoding='utf-8').read()).group(1)
    for f in files: compile_tex(f)
    for lang in ('en', 'fr'):
        build_txt(f'{HERE}/{EXTRACTS[lang]}', f'{HERE}/{EXTRACTS[lang][:-4]}.txt', TXT_HEAD[lang], tag, lang)
    print('version tag:', tag)

if __name__ == '__main__':
    main()
