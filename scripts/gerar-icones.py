# -*- coding: utf-8 -*-
"""Gera a grade de icones da stack (assets/social/stack.svg).

Os desenhos vem do Simple Icons (CC0), baixados uma vez para
scripts/icones-simple-icons.json. Para incluir outro:

    curl -s https://cdn.simpleicons.org/<slug>   # devolve cor da marca e path

Cor: a da marca, mas clareada quando escura demais para o fundo roxo — sem
isso, Next.js, GitHub e Express somem no tile. O skillicons contorna o mesmo
problema usando fundo claro atras do icone.

VS Code nao entra: a Microsoft pediu a remocao do icone do Simple Icons.
"""
import json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
ICONES = json.load(open(os.path.join(RAIZ, "scripts", "icones-simple-icons.json"), encoding="utf-8"))

# ordem = do que ele mais escreve para o que menos, depois ferramentas
ORDEM = ["PHP","JavaScript","TypeScript","Python","HTML","CSS","jQuery","Bootstrap","React",
         "Next.js","Redux","Tailwind","Node.js","Express","FastAPI","MySQL","PostgreSQL",
         "SQLite","Redis","Vite","Vitest","Git","GitHub","Figma","Linux","Kali","Bash"]

TILE, GAP, PAD, POR_LINHA, ICONE = 48.0, 10.0, 18.0, 14, 25.0
PISO_LUM = 0.42          # luminancia minima do icone sobre o tile escuro

def clarear(hexa):
    """Mistura a cor da marca com branco ate ela ficar legivel no fundo escuro."""
    r, g, b = (int(hexa[i:i+2], 16) for i in (1, 3, 5))
    lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
    if lum >= PISO_LUM:
        return hexa
    t = min((PISO_LUM - lum) / (1 - lum) + 0.12, 1.0)   # fracao de branco
    r, g, b = (round(c + (255 - c) * t) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


linhas = (len(ORDEM) + POR_LINHA - 1) // POR_LINHA
W = PAD * 2 + POR_LINHA * TILE + (POR_LINHA - 1) * GAP
H = PAD * 2 + linhas * TILE + (linhas - 1) * GAP

pecas = []
for i, nome in enumerate(ORDEM):
    col, lin = i % POR_LINHA, i // POR_LINHA
    x = PAD + col * (TILE + GAP)
    y = PAD + lin * (TILE + GAP)
    ix, iy = x + (TILE - ICONE) / 2, y + (TILE - ICONE) / 2
    pecas.append(
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{TILE}" height="{TILE}" rx="11" fill="#1b0733"/>'
        f'<rect x="{x+.5:.1f}" y="{y+.5:.1f}" width="{TILE-1}" height="{TILE-1}" rx="10.5" '
        f'fill="none" stroke="#7b2cbf" stroke-opacity=".35"/>'
        f'<g transform="translate({ix:.1f},{iy:.1f}) scale({ICONE/24:.4f})"><title>{nome}</title>'
        f'<path d="{ICONES[nome]["d"]}" fill="{clarear(ICONES[nome]["cor"])}"/></g>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" '
       f'viewBox="0 0 {W:.1f} {H:.1f}" role="img" aria-label="{", ".join(ORDEM)}">'
       f'<title>stack</title>{"".join(pecas)}</svg>\n')
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "stack.svg"), "w", encoding="utf-8").write(svg)
print(f"stack.svg  {W:.0f}x{H:.0f}  {len(svg)/1024:.0f} KB  ({len(ORDEM)} icones)")
