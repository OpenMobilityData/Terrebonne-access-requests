#!/usr/bin/env python3
"""Black out the requester's personal information on the pages of a PDF before publication (owner's rule, Nov 6, 2026:
the name stays; e-mail address, home address and telephone number are always redacted).
Boxes come from the PDF's own text layer (pdftotext -bbox-layout): whole-line boxes for the address lines, word boxes for
the e-mail and phone tokens (with a bare area code beside the number). Each treated page is rasterized at 300 dpi and
written back as an image page; the other pages are kept as in the original (qpdf). Prints every box drawn.
Usage: redact_owner_info.py <in.pdf> <out.pdf> --pages 1,2,3 [--email rickhoge] [--phone 562-8459] [--address "Ponsard|H3W 2A6|^4931"]
"""
import argparse, os, re, subprocess, tempfile, xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
ap = argparse.ArgumentParser(); ap.add_argument('src'); ap.add_argument('out'); ap.add_argument('--pages', required=True)
ap.add_argument('--email', default='rickhoge'); ap.add_argument('--phone', default=r'562[- .]?8459'); ap.add_argument('--address', default=r'Ponsard|H3W\s*2A6|^4931')
A = ap.parse_args()
DPI = 300; K = DPI / 72.0; PAD = 4
word_pats = [re.compile(A.email, re.I), re.compile(A.phone, re.I)]; area = re.compile(r'^\(?514\)?$')
line_pat = re.compile(A.address, re.I)
pages = [int(p) for p in A.pages.split(',')]
tmp = tempfile.mkdtemp(); parts = []
npages = int(subprocess.run(['pdfinfo', A.src], capture_output=True, text=True).stdout.split('Pages:')[1].split()[0])
NS = '{http://www.w3.org/1999/xhtml}'
for p in range(1, npages + 1):
    if p not in pages:
        parts += [A.src, str(p)]; continue
    subprocess.run(['pdftoppm', '-r', str(DPI), '-png', '-f', str(p), '-l', str(p), A.src, os.path.join(tmp, f'pg{p}')], check=True, stderr=subprocess.DEVNULL)
    png = [os.path.join(tmp, f) for f in os.listdir(tmp) if f.startswith(f'pg{p}') and f.endswith('.png')][0]
    xmlp = os.path.join(tmp, f'p{p}.xml')
    subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-bbox-layout', A.src, xmlp], check=True, stderr=subprocess.DEVNULL)
    root = ET.parse(xmlp).getroot()
    img = Image.open(png).convert('RGB'); draw = ImageDraw.Draw(img); n = 0
    def box(elems, label):
        global n
        x0 = min(float(e.get('xMin')) for e in elems) * K - PAD; y0 = min(float(e.get('yMin')) for e in elems) * K - PAD
        x1 = max(float(e.get('xMax')) for e in elems) * K + PAD; y1 = max(float(e.get('yMax')) for e in elems) * K + PAD
        draw.rectangle([x0, y0, x1, y1], fill='black'); n += 1; print(f'  p.{p} blacked out {label!r}')
    for line in root.iter(NS + 'line'):
        words = list(line.iter(NS + 'word')); text = ' '.join((w.text or '') for w in words)
        if line_pat.search(text):
            box([line], text); continue
        hit = [w for w in words if any(pt.search(w.text or '') for pt in word_pats)]
        for w in list(hit):
            i = words.index(w)
            if i > 0 and area.search(words[i - 1].text or ''): hit.append(words[i - 1])
        if hit: box(hit, ' '.join((w.text or '') for w in hit))
    outp = os.path.join(tmp, f'red{p}.pdf'); img.save(outp, 'PDF', resolution=float(DPI)); parts += [outp, '1']
    print(f'  p.{p}: {n} box(es)')
cmd = ['qpdf', '--empty', '--pages']
for i in range(0, len(parts), 2): cmd += [parts[i], parts[i + 1]]
cmd += ['--', A.out]
rc = subprocess.run(cmd, stderr=subprocess.DEVNULL).returncode
if rc not in (0, 3): raise SystemExit(f'qpdf failed with code {rc}')   # 3 = succeeded with warnings
print('wrote', A.out)
