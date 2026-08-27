# -*- coding: utf-8 -*-
"""Gera o cartao de linguagens (assets/social/linguagens.svg).

Os numeros sao agregados dos repositorios e ficam congelados no arquivo, por
isso o cartao mostra a data do levantamento. Para atualizar:

    gh repo list <user> --limit 50 --json name -q '.[].name' | while read r; do
      gh api repos/<user>/$r/languages; done

...e some os bytes por linguagem no dicionario DADOS abaixo.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"

DATA = "agosto de 2026"
REPOS = 20
DADOS = [("PHP", 59.4, "#c77dff"), ("TypeScript", 14.0, "#b45ce8"), ("Python", 13.4, "#d95fd0"),
         ("CSS", 4.5, "#ef62b8"), ("HTML", 4.0, "#ff79c6"), ("JavaScript", 3.0, "#ff9ad5"),
         ("outras", 1.7, "#4a1580")]

W, H = 900, 196
PAD = 30
BARRA_Y, BARRA_H = 78, 20

barra, x = [], PAD
larg_util = W - PAD * 2
for i, (nome, pct, cor) in enumerate(DADOS):
    w = larg_util * pct / 100
    barra.append(f'<rect x="{x:.1f}" y="{BARRA_Y}" width="{max(w - 2, 1):.1f}" height="{BARRA_H}" rx="4" fill="{cor}"/>')
    x += w

legenda, lx, ly = [], PAD, 132
for i, (nome, pct, cor) in enumerate(DADOS[:6]):
    col, lin = i % 3, i // 3
    px = PAD + col * (larg_util / 3)
    py = ly + lin * 26
    legenda.append(
        f'<rect x="{px:.0f}" y="{py - 10:.0f}" width="11" height="11" rx="2.5" fill="{cor}"/>'
        f'<text x="{px + 19:.0f}" y="{py:.0f}" font-family="{MONO}" font-size="13" fill="#e6edf3">{nome}</text>'
        f'<text x="{px + larg_util/3 - 46:.0f}" y="{py:.0f}" font-family="{MONO}" font-size="13" '
        f'font-weight="bold" fill="#ff79c6" text-anchor="end">{pct:.1f}%</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Distribuição de linguagens: PHP 59,4%, TypeScript 14%, Python 13,4%">
  <title>linguagens por volume de código</title>
  <defs>
    <linearGradient id="fundo_lang" x1="0" y1="0" x2=".7" y2="1">
      <stop offset="0" stop-color="#15012e"/><stop offset="1" stop-color="#0b0018"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="14" fill="url(#fundo_lang)"/>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="13.25" fill="none" stroke="#7b2cbf" stroke-opacity=".45"/>

  <text x="{PAD}" y="42" font-family="{MONO}" font-size="14" xml:space="preserve"><tspan fill="#7b2cbf">└─$ </tspan><tspan fill="#ffffff">cat linguagens.txt</tspan></text>
  <text x="{W - PAD}" y="42" font-family="{MONO}" font-size="11.5" fill="#8b7aa8" text-anchor="end">{REPOS} repositórios · {DATA}</text>

  {"".join(barra)}
  {"".join(legenda)}
</svg>
'''
open(os.path.join(OUT, "linguagens.svg"), "w", encoding="utf-8").write(svg)
print(f"linguagens.svg  {W}x{H}")
