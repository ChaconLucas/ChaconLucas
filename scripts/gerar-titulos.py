# -*- coding: utf-8 -*-
"""Gera os titulos de secao do README (assets/social/titulos/).

Motivo: o banner tem tipografia propria e o resto do README caia na fonte
padrao do GitHub — a pagina se partia em duas no meio. Estes titulos usam a
mesma monoespacada e a mesma paleta do banner.

Rode `python3 scripts/gerar-titulos.py` ao mudar texto ou cor.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social", "titulos")
os.makedirs(OUT, exist_ok=True)

MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"
LARG, ALT, FS = 900, 46, 19.0

SECOES = [("whoami", "whoami"), ("stack", "stack"), ("metricas", "métricas"),
          ("contribuicoes", "contribuições"), ("experiencia", "experiência"),
          ("projetos", "projetos em destaque"), ("contato", "contato"),
          ("tiix", "tiix 2.0"), ("pessoais", "projetos pessoais"), ("outros", "outros projetos")]
# so os que mudam de texto em ingles; whoami, stack e tiix 2.0 servem aos dois
SECOES_EN = [("pessoais", "side projects"), ("outros", "other projects")]
OUT_EN = os.path.join(RAIZ, "assets", "social", "en", "titulos")


def titulo(nome, texto, out):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{LARG}" height="{ALT}" viewBox="0 0 {LARG} {ALT}" role="img" aria-label="{texto}">
  <title>{texto}</title>
  <defs>
    <linearGradient id="txt_{nome}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#c77dff"/><stop offset="1" stop-color="#9d4edd"/>
    </linearGradient>
    <linearGradient id="fio_{nome}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#7b2cbf" stop-opacity=".85"/>
      <stop offset="1" stop-color="#7b2cbf" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <text x="0" y="24" font-family="{MONO}" font-size="{FS}" font-weight="bold" fill="#7b2cbf">&gt;_</text>
  <text x="{3 * FS * 0.6 + 6:.0f}" y="24" font-family="{MONO}" font-size="{FS}" font-weight="bold" fill="url(#txt_{nome})">{texto}</text>
  <rect x="0" y="36" width="{LARG}" height="1.5" fill="url(#fio_{nome})"/>
</svg>
'''
    open(os.path.join(out, nome + ".svg"), "w", encoding="utf-8").write(svg)
    print(os.path.relpath(os.path.join(out, nome + ".svg"), RAIZ))


for nome, texto in SECOES:
    titulo(nome, texto, OUT)
for nome, texto in SECOES_EN:
    titulo(nome, texto, OUT_EN)


# --- rotulos menores, para subdivisao dentro de uma secao ------------------
# o <sub> do HTML cai na fonte padrao do GitHub e destoa; este acompanha a
# tipografia dos titulos, so que menor e sem o fio.
ROTULOS = [("ferramentas", "bibliotecas e ferramentas"),
           ("stack-atual", "no dia a dia"),
           ("tambem", "também já trabalhei com"),
           ("contribuicoes", "~18.900 contribuições no último ano, a maioria em repositórios privados da empresa")]
ROTULOS_EN = [("stack-atual", "day to day"),
              ("tambem", "I have also worked with"),
              ("contribuicoes", "~18,900 contributions in the last year, most of them in the company's private repos")]


def rotulo(nome, texto, out):
    fs = 13.0
    larg = len(texto) * fs * 0.6 + 30
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{larg:.0f}" height="26" viewBox="0 0 {larg:.0f} 26" role="img" aria-label="{texto}">
  <title>{texto}</title>
  <text x="0" y="18" font-family="{MONO}" font-size="{fs}" fill="#7b2cbf">»</text>
  <text x="18" y="18" font-family="{MONO}" font-size="{fs}" fill="#8b7aa8">{texto.replace("'", "&#39;")}</text>
</svg>
'''
    open(os.path.join(out, "rotulo-" + nome + ".svg"), "w", encoding="utf-8").write(svg)
    print(os.path.relpath(os.path.join(out, "rotulo-" + nome + ".svg"), RAIZ))


for nome, texto in ROTULOS:
    rotulo(nome, texto, OUT)
for nome, texto in ROTULOS_EN:
    rotulo(nome, texto, OUT_EN)
