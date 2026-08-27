# -*- coding: utf-8 -*-
"""Gera o heatmap de contribuicoes (assets/social/contribuicoes.svg).

Os dados sao assados aqui: uma linha por semana, um digito por dia, com o
nivel de 0 a 4 (quartis dos dias com atividade). Para atualizar:

    gh api graphql -f query='{user(login:"ChaconLucas"){contributionsCollection
      {contributionCalendar{totalContributions weeks{contributionDays
      {date contributionCount}}}}}}'

...e recalcule os niveis pelos quartis dos dias com contribuicao.
Levantamento congela na data, por isso o rodape do cartao mostra o periodo.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"

TOTAL = 9528
PERIODO = "ago/2025 — ago/2026"
NIVEIS = """0000000
0000000
0000000
0000000
0000000
0000000
0000000
0000000
0000000
0000000
0000000
0000000
0000000
0101020
0121100
0011000
0121010
0000000
0010000
0000000
0000000
0000000
0000110
0122130
1220100
0000000
0121200
0021200
0122100
0000210
2222112
0111110
0000000
0110110
0102021
0333400
0233340
0233440
0444444
4444330
1334143
4442321
4444233
2222434
1320200
0320200
0321340
0442404
3434420
0333423
0333433
2343431
04343.."""
MESES = [(0, '2025-08-24'), (1, '2025-08-31'), (2, '2025-09-07'), (3, '2025-09-14'), (4, '2025-09-21'), (5, '2025-09-28'), (6, '2025-10-05'), (7, '2025-10-12'), (8, '2025-10-19'), (9, '2025-10-26'), (10, '2025-11-02'), (11, '2025-11-09'), (12, '2025-11-16'), (13, '2025-11-23'), (14, '2025-11-30'), (15, '2025-12-07'), (16, '2025-12-14'), (17, '2025-12-21'), (18, '2025-12-28'), (19, '2026-01-04'), (20, '2026-01-11'), (21, '2026-01-18'), (22, '2026-01-25'), (23, '2026-02-01'), (24, '2026-02-08'), (25, '2026-02-15'), (26, '2026-02-22'), (27, '2026-03-01'), (28, '2026-03-08'), (29, '2026-03-15'), (30, '2026-03-22'), (31, '2026-03-29'), (32, '2026-04-05'), (33, '2026-04-12'), (34, '2026-04-19'), (35, '2026-04-26'), (36, '2026-05-03'), (37, '2026-05-10'), (38, '2026-05-17'), (39, '2026-05-24'), (40, '2026-05-31'), (41, '2026-06-07'), (42, '2026-06-14'), (43, '2026-06-21'), (44, '2026-06-28'), (45, '2026-07-05'), (46, '2026-07-12'), (47, '2026-07-19'), (48, '2026-07-26'), (49, '2026-08-02'), (50, '2026-08-09'), (51, '2026-08-16'), (52, '2026-08-23')]

CORES = ["#1c0838", "#4a1580", "#7b2cbf", "#b45ce8", "#e0c3fc"]
CELULA, GAP = 12.0, 3.0
PAD_ESQ, PAD_TOPO = 34, 46

NOMES_MES = {"01":"jan","02":"fev","03":"mar","04":"abr","05":"mai","06":"jun",
             "07":"jul","08":"ago","09":"set","10":"out","11":"nov","12":"dez"}
DIAS = {1: "seg", 3: "qua", 5: "sex"}

semanas = NIVEIS.strip().split("\n")
W = int(PAD_ESQ + len(semanas) * (CELULA + GAP) + 20)
H = int(PAD_TOPO + 7 * (CELULA + GAP) + 46)

celulas = []
for x, semana in enumerate(semanas):
    for y, ch in enumerate(semana):
        if ch == ".":
            continue
        cx = PAD_ESQ + x * (CELULA + GAP)
        cy = PAD_TOPO + y * (CELULA + GAP)
        celulas.append(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{CELULA}" height="{CELULA}" '
                       f'rx="2.5" fill="{CORES[int(ch)]}"/>')

# rotulo de mes na primeira semana de cada mes
rotulos, visto = [], set()
for i, dia in MESES:
    mes = dia[5:7]
    if mes in visto:
        continue
    visto.add(mes)
    x = PAD_ESQ + i * (CELULA + GAP)
    rotulos.append(f'<text x="{x:.0f}" y="{PAD_TOPO - 8}" font-family="{MONO}" font-size="10.5" '
                   f'fill="#8b7aa8">{NOMES_MES[mes]}</text>')

for y, nome in DIAS.items():
    cy = PAD_TOPO + y * (CELULA + GAP) + CELULA - 2
    rotulos.append(f'<text x="0" y="{cy:.0f}" font-family="{MONO}" font-size="10" fill="#8b7aa8">{nome}</text>')

# legenda
lx = W - 20 - 5 * (CELULA + GAP) - 46
ly = H - 20
legenda = [f'<text x="{lx - 8:.0f}" y="{ly:.0f}" font-family="{MONO}" font-size="10.5" '
           f'fill="#8b7aa8" text-anchor="end">menos</text>']
for i, cor in enumerate(CORES):
    legenda.append(f'<rect x="{lx + i * (CELULA + GAP):.1f}" y="{ly - 10:.0f}" width="{CELULA}" '
                   f'height="{CELULA}" rx="2.5" fill="{cor}"/>')
legenda.append(f'<text x="{lx + 5 * (CELULA + GAP) + 6:.0f}" y="{ly:.0f}" font-family="{MONO}" '
               f'font-size="10.5" fill="#8b7aa8">mais</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{TOTAL} contribuições entre {PERIODO}">
  <title>{TOTAL} contribuições · {PERIODO}</title>
  <defs><linearGradient id="fundo_c" x1="0" y1="0" x2=".7" y2="1">
    <stop offset="0" stop-color="#191526"/><stop offset="1" stop-color="#14111e"/>
  </linearGradient></defs>
  <rect width="{W}" height="{H}" rx="14" fill="url(#fundo_c)"/>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="13.25" fill="none" stroke="#3d2b5c"/>
  <g transform="translate(20,10)">
    <text x="0" y="24" font-family="{MONO}" font-size="14" xml:space="preserve"><tspan fill="#7b2cbf">└─$ </tspan><tspan fill="#ffffff">git log --graph --all</tspan></text>
    <text x="{W - 40}" y="24" font-family="{MONO}" font-size="11.5" fill="#8b7aa8" text-anchor="end">{TOTAL} contribuições · {PERIODO}</text>
    {"".join(rotulos)}
    {"".join(celulas)}
    {"".join(legenda)}
  </g>
</svg>
'''
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "contribuicoes.svg"), "w", encoding="utf-8").write(svg)
print(f"contribuicoes.svg  {W}x{H}")
