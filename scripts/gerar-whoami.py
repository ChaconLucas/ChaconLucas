# -*- coding: utf-8 -*-
"""Gera o cartao do whoami (assets/social/whoami.svg).

Mesmo padrao dos cartoes de linguagens e contribuicoes: painel com borda
roxa e a linha `└─$ comando` no topo. O JSON e colorido por papel — chave,
string e pontuacao — como um editor faria.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"

CHAVE, STRING, PONT, CMD = "#c77dff", "#e0c3fc", "#7b2cbf", "#ffffff"

CAMPOS = [("formacao", "Análise e Desenvolvimento de Sistemas — UNISUAM"),
          ("pos",      "Cibersegurança (Pentest · Kali Linux)"),
          ("atuacao",  "Full Stack — do banco de dados ao deploy"),
          ("foco",     "produtos, não páginas")]

FS, LH, PAD = 13.5, 22.0, 30.0
W = 900

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

linhas = []
y = PAD + 34
larg_chave = max(len(c) for c, _ in CAMPOS) + 3

linhas.append(f'<text x="{PAD}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{PONT}">{{</text>')
y += LH
for i, (chave, valor) in enumerate(CAMPOS):
    virg = "," if i < len(CAMPOS) - 1 else ""
    rotulo = f'"{chave}":'.ljust(larg_chave + 3)
    linhas.append(
        f'<text x="{PAD + 22}" y="{y}" font-family="{MONO}" font-size="{FS}" xml:space="preserve">'
        f'<tspan fill="{CHAVE}">{esc(rotulo)}</tspan>'
        f'<tspan fill="{STRING}">"{esc(valor)}"</tspan>'
        f'<tspan fill="{PONT}">{virg}</tspan></text>')
    y += LH
linhas.append(f'<text x="{PAD}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{PONT}">}}</text>')
H = int(y + PAD - 4)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{"; ".join(f"{c}: {v}" for c, v in CAMPOS)}">
  <title>whoami</title>
  <defs><linearGradient id="fundo_w" x1="0" y1="0" x2=".7" y2="1">
    <stop offset="0" stop-color="#15012e"/><stop offset="1" stop-color="#0b0018"/>
  </linearGradient></defs>
  <rect width="{W}" height="{H}" rx="14" fill="url(#fundo_w)"/>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="13.25" fill="none" stroke="#7b2cbf" stroke-opacity=".45"/>
  <text x="{PAD}" y="{PAD + 12}" font-family="{MONO}" font-size="14" xml:space="preserve"><tspan fill="{PONT}">└─$ </tspan><tspan fill="{CMD}">cat lucas.json</tspan></text>
  {"".join(linhas)}
</svg>
'''
open(os.path.join(OUT, "whoami.svg"), "w", encoding="utf-8").write(svg)
print(f"whoami.svg  {W}x{H}")
