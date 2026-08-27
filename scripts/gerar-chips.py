# -*- coding: utf-8 -*-
"""Gera as pilulas de tecnologia dos cards (assets/social/chips/).

Le o proprio README, acha as linhas que sao so code spans (a linha de stack
de cada card) e gera um SVG por tecnologia. Rodar de novo depois de incluir
um projeto novo cria as pilulas que faltarem.
"""
import os, re, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social", "chips")
os.makedirs(OUT, exist_ok=True)

MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"
FS, ALT_PILL, MARGEM = 11.0, 22.0, 3.0
PAD = 11.0

def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def chip(texto):
    w_txt = len(texto) * FS * 0.6 + 0.3 * (len(texto) - 1)
    pw = w_txt + PAD * 2
    W, H = pw + MARGEM * 2, ALT_PILL + MARGEM * 2
    r = ALT_PILL / 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.1f} {H:.1f}" role="img" aria-label="{texto}">
  <title>{texto}</title>
  <rect x="{MARGEM}" y="{MARGEM}" width="{pw:.1f}" height="{ALT_PILL}" rx="{r}" fill="#2a0a4d"/>
  <rect x="{MARGEM+.5}" y="{MARGEM+.5}" width="{pw-1:.1f}" height="{ALT_PILL-1}" rx="{r-.5}" fill="none" stroke="#7b2cbf" stroke-opacity=".55"/>
  <text x="{MARGEM + pw/2:.1f}" y="{MARGEM + ALT_PILL/2:.1f}" dy=".35em" text-anchor="middle"
        font-family="{MONO}" font-size="{FS}" letter-spacing=".3" fill="#d9b8ff">{texto}</text>
</svg>
'''

readme = open(os.path.join(RAIZ, "README.md"), encoding="utf-8").read()
# linha que e so code spans = linha de stack de um card
tecs = []
for linha in readme.split("\n"):
    if re.fullmatch(r"(`[^`]+`\s*)+", linha.strip()) and linha.strip():
        tecs += re.findall(r"`([^`]+)`", linha)
tecs = sorted(set(tecs))
for t in tecs:
    open(os.path.join(OUT, slug(t) + ".svg"), "w", encoding="utf-8").write(chip(t))
print(f"{len(tecs)} pilulas: {', '.join(tecs)}")
