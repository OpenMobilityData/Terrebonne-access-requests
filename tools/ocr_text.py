#!/usr/bin/env python3
"""Full text of every PDF in a release's raw/ folder, so the whole release can be searched.

For each PDF in <request>/raw/ (subfolders included) it writes <request>/derived/ocr/<same relative path>.txt:
one block per page, headed « === page N (text layer) === » or « === page N (OCR) === ».
  - pages whose own text layer holds at least MIN_CHARS characters: that text layer (pdftotext -layout), unchanged;
  - the other pages (scans, and pages flattened to images by redaction): read by Tesseract at 300 dpi with the
    French and English models (tessdata_best). OCR text is a machine reading, unchecked: quote from the page image.
The raw/ files are never modified. Redacted areas are black boxes and yield no text.
A run also prints a check for the owner's personal information (none may appear in a public file).

Usage: python3 tools/ocr_text.py 2026-581 [2026-634 …]   (TESSDATA_PREFIX defaults to ~/Terrebonne-data/third-party/tessdata)
Needs pdftotext/pdftoppm (Poppler) and tesseract."""
import os, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

MIN_CHARS = 120
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('TESSDATA_PREFIX', os.path.expanduser('~/Terrebonne-data/third-party/tessdata'))
PII = re.compile(r'rickhoge@|Ponsard|562-8459', re.I)


def npages(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    m = re.search(r'^Pages:\s+(\d+)', out, re.M)
    return int(m.group(1)) if m else 0


def text_layer(pdf, p):
    return subprocess.run(['pdftotext', '-q', '-layout', '-f', str(p), '-l', str(p), pdf, '-'],
                          capture_output=True, text=True).stdout


def ocr(pdf, p):
    with tempfile.TemporaryDirectory() as td:
        base = os.path.join(td, 'pg')
        subprocess.run(['pdftoppm', '-q', '-r', '300', '-gray', '-png', '-f', str(p), '-l', str(p), pdf, base], check=True)
        png = sorted(f for f in os.listdir(td) if f.endswith('.png'))[0]
        return subprocess.run(['tesseract', os.path.join(td, png), 'stdout', '-l', 'fra+eng'],
                              capture_output=True, text=True).stdout


def page(pdf, p):
    t = text_layer(pdf, p)
    if len(t.strip()) >= MIN_CHARS:
        return p, 'text layer', t
    return p, 'OCR', ocr(pdf, p)


def one(pdf, out):
    n = npages(pdf)
    with ThreadPoolExecutor(max_workers=10) as ex:
        pages = sorted(ex.map(lambda p: page(pdf, p), range(1, n + 1)))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        for p, how, t in pages:
            f.write(f'=== page {p} ({how}) ===\n{t.rstrip()}\n\n')
    k = sum(1 for _, how, _ in pages if how == 'OCR')
    return n, k


def main(reqs):
    for req in reqs:
        raw = os.path.join(ROOT, req, 'raw')
        for dp, _, fs in os.walk(raw):
            for fn in sorted(fs):
                if not fn.lower().endswith('.pdf'):
                    continue
                pdf = os.path.join(dp, fn)
                rel = os.path.relpath(pdf, raw)
                out = os.path.join(ROOT, req, 'derived', 'ocr', rel + '.txt')
                n, k = one(pdf, out)
                hit = PII.search(open(out, encoding='utf-8').read())
                print(f'{req}/raw/{rel}: {n} pages, {k} by OCR' + ('  !! PERSONAL INFORMATION FOUND' if hit else ''), flush=True)


if __name__ == '__main__':
    main(sys.argv[1:] or sorted(d for d in os.listdir(ROOT) if re.match(r'20\d\d-\d+$', d)))
