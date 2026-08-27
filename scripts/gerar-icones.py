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
ORDEM = ["PHP","JavaScript","TypeScript","Python","HTML","CSS","jQuery","Bootstrap",
         "React","Next.js","Node.js","Express","FastAPI","MySQL","PostgreSQL","Kali"]

# apoio: biblioteca, build, teste, editor e ambiente. Entram menores e em uma
# cor so — hierarquia: a stack diz o que ele constroi, isto diz com o que.
APOIO = ["Redux","Tailwind","SQLite","Redis","Vite","Vitest","Git","GitHub","Figma","Linux","Bash"]

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


def grade(arquivo, nomes, tile, por_linha, mono=None, rotulo=None, com_tile=False):
    """Tile redondo e neutro: a moldura volta para normalizar o tamanho
    aparente dos icones (MySQL e Kali sao largos e baixos, e sem caixa
    pareciam menores), mas sem o fio roxo, que somava ruido em 27 copias.
    O raio total conversa com as pilulas dos botoes e dos chips."""
    gap, pad = 9.0, 16.0
    icone = tile * 0.54
    linhas = (len(nomes) + por_linha - 1) // por_linha
    W = pad * 2 + por_linha * tile + (por_linha - 1) * gap
    topo = pad + (18 if rotulo else 0)
    H = topo + linhas * tile + (linhas - 1) * gap + pad
    pecas = []
    if rotulo:
        pecas.append(f'<text x="{pad}" y="{pad + 6:.0f}" font-family="DejaVu Sans Mono,Menlo,monospace" '
                     f'font-size="11.5" fill="#8b949e">{rotulo}</text>')
    for i, nome in enumerate(nomes):
        col, lin = i % por_linha, i // por_linha
        x = pad + col * (tile + gap)
        y = topo + lin * (tile + gap)
        ix, iy = x + (tile - icone) / 2, y + (tile - icone) / 2
        cor = mono or clarear(ICONES[nome]["cor"])
        pecas.append(
            f'<circle cx="{x + tile/2:.1f}" cy="{y + tile/2:.1f}" r="{tile/2:.1f}" fill="#1d1a2b"/>')
        pecas.append(
            f'<g transform="translate({ix:.1f},{iy:.1f}) scale({icone/24:.4f})"><title>{nome}</title>'
            f'<path d="{ICONES[nome]["d"]}" fill="{cor}"/></g>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" '
           f'viewBox="0 0 {W:.1f} {H:.1f}" role="img" aria-label="{", ".join(nomes)}">'
           f'<title>{rotulo or "stack"}</title>{"".join(pecas)}</svg>\n')
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, arquivo), "w", encoding="utf-8").write(svg)
    print(f"{arquivo}  {W:.0f}x{H:.0f}  ({len(nomes)} icones)")


grade("stack.svg", ORDEM, tile=50.0, por_linha=16)
grade("ferramentas.svg", APOIO, tile=38.0, por_linha=16, mono="#9d7bc4",
      rotulo="bibliotecas e ferramentas")
