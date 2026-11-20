# -*- coding: utf-8 -*-
"""Gera o cartao da Tiix 2.0 (assets/social/tiix.svg e en/tiix.svg).

Mesmo painel do whoami e das camadas: fundo escuro, borda roxa e a linha
`└─$ comando` no topo. Em cima, os numeros em destaque; embaixo, a stack
como pares chave/valor. So entra o que e publico.

Rode `python3 scripts/gerar-tiix.py` ao atualizar os numeros.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"

ROTULO, TEXTO, PONT, CMD, COMENT, FIO = "#c77dff", "#e6edf3", "#7b2cbf", "#ffffff", "#8b7aa8", "#3d2b5c"

IDIOMAS = {
    "pt": dict(
        saida=os.path.join(OUT, "tiix.svg"),
        comando="tiix --em-numeros",
        numeros=[("1.600+", "PRs"), ("260", "tabelas"), ("450", "migrations"),
                 ("2", "apps"), ("zero", "downtime no deploy")],
        pares=[("web",   "Next.js"),
               ("api",   "NestJS + Prisma + PostgreSQL"),
               ("apps",  "Tiix e Tiix Pro · Expo / React Native · TestFlight, indo para as lojas"),
               ("infra", "CI e deploy próprios numa VPS")],
        comentario="ecossistema de saúde: clientes, profissionais, clínicas e corretoras, reconstruído do zero",
    ),
    "en": dict(
        saida=os.path.join(OUT, "en", "tiix.svg"),
        comando="tiix --by-the-numbers",
        numeros=[("1,600+", "PRs"), ("260", "tables"), ("450", "migrations"),
                 ("2", "apps"), ("zero", "deploy downtime")],
        pares=[("web",   "Next.js"),
               ("api",   "NestJS + Prisma + PostgreSQL"),
               ("apps",  "Tiix and Tiix Pro · Expo / React Native · TestFlight, heading to the stores"),
               ("infra", "in-house CI and deploy on a VPS")],
        comentario="a health ecosystem: clients, professionals, clinics and brokers, rebuilt from scratch",
    ),
}

W, PAD = 900, 30.0


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def gerar(saida, comando, numeros, pares, comentario):
    partes = []
    # --- faixa de numeros: colunas iguais, separadas por um fio -------------
    topo = PAD + 34
    col = (W - 2 * PAD) / len(numeros)
    for i, (num, rot) in enumerate(numeros):
        cx = PAD + col * i + col / 2
        partes.append(f'<text x="{cx:.1f}" y="{topo + 30:.1f}" text-anchor="middle" font-family="{MONO}" '
                      f'font-size="30" font-weight="bold" fill="url(#num_t)">{esc(num)}</text>')
        partes.append(f'<text x="{cx:.1f}" y="{topo + 52:.1f}" text-anchor="middle" font-family="{MONO}" '
                      f'font-size="12" fill="{COMENT}">{esc(rot)}</text>')
        if i:
            x = PAD + col * i
            partes.append(f'<rect x="{x:.1f}" y="{topo + 4:.1f}" width="1" height="52" fill="{FIO}"/>')
    y = topo + 90

    # --- pares chave/valor, no padrao das camadas ----------------------------
    larg = max(len(c) for c, _ in pares)
    for chave, valor in pares:
        pontos = "." * (larg + 2 - len(chave))
        partes.append(
            f'<text x="{PAD}" y="{y:.0f}" font-family="{MONO}" font-size="12.5" xml:space="preserve">'
            f'<tspan fill="{ROTULO}">{chave} </tspan><tspan fill="{PONT}">{pontos}</tspan>'
            f'<tspan fill="{TEXTO}"> {esc(valor)}</tspan></text>')
        y += 23
    y += 8
    partes.append(f'<text x="{PAD}" y="{y:.0f}" font-family="{MONO}" font-size="12" fill="{COMENT}" '
                  f'xml:space="preserve"># {esc(comentario)}</text>')
    H = int(y + PAD - 8)

    rotulo = "; ".join(f"{n} {r}" for n, r in numeros)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Tiix 2.0: {esc(rotulo)}">
  <title>Tiix 2.0</title>
  <defs>
    <linearGradient id="fundo_t" x1="0" y1="0" x2=".7" y2="1">
      <stop offset="0" stop-color="#191526"/><stop offset="1" stop-color="#14111e"/>
    </linearGradient>
    <linearGradient id="num_t" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#e0c3fc"/><stop offset="1" stop-color="#c77dff"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="14" fill="url(#fundo_t)"/>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="13.25" fill="none" stroke="{FIO}"/>
  <text x="{PAD}" y="{PAD + 12}" font-family="{MONO}" font-size="14" xml:space="preserve"><tspan fill="{PONT}">└─$ </tspan><tspan fill="{CMD}">{comando}</tspan></text>
  {"".join(partes)}
</svg>
'''
    open(saida, "w", encoding="utf-8").write(svg)
    print(f"{os.path.relpath(saida, RAIZ)}  {W}x{H}")


for cfg in IDIOMAS.values():
    gerar(**cfg)
