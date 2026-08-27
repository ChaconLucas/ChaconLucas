# -*- coding: utf-8 -*-
"""Gera o hero do topo e o rodape do README (assets/social/).

Tudo em monoespacada de proposito: a identidade da pagina e terminal.
Rode `python3 scripts/gerar-hero.py` depois de mexer em texto ou cor.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
os.makedirs(OUT, exist_ok=True)

MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"

def mono_w(t, fs, ls=0.0):
    """Monoespacada: largura previsivel, entao da pra fixar com textLength."""
    return len(t) * fs * 0.6 + ls * (len(t) - 1)

def texto(t, x, y, fs, cor, ls=0.0, peso="normal", anchor="start"):
    w = mono_w(t, fs, ls)
    x2 = x - w / 2 if anchor == "middle" else x
    return (f'<text x="{x2:.1f}" y="{y:.1f}" font-family="{MONO}" font-size="{fs}" font-weight="{peso}" '
            f'letter-spacing="{ls}" fill="{cor}" textLength="{w:.1f}" lengthAdjust="spacing">{t}</text>')

# --- hero ------------------------------------------------------------------
W, H = 1000, 250

# janelinha de terminal decorativa no canto direito
tx, ty, tw, th = 612, 54, 330, 142
barras = [(196, "#7b2cbf", .95), (128, "#c77dff", .55), (238, "#5a189a", .9),
          (96, "#c77dff", .35), (168, "#7b2cbf", .7)]
codigo = "".join(
    f'<rect x="{tx+20}" y="{ty+52+i*17}" width="{lw}" height="7" rx="3.5" fill="{c}" opacity="{o}"/>'
    for i, (lw, c, o) in enumerate(barras))

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Lucas Chacon — full stack developer">
  <title>Lucas Chacon — full stack developer</title>
  <defs>
    <linearGradient id="fundo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#10002b"/><stop offset=".55" stop-color="#240046"/><stop offset="1" stop-color="#3c096c"/>
    </linearGradient>
    <radialGradient id="halo" cx=".78" cy=".18" r=".55">
      <stop offset="0" stop-color="#7b2cbf" stop-opacity=".45"/><stop offset="1" stop-color="#7b2cbf" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="risco" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#c77dff"/><stop offset="1" stop-color="#c77dff" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grade" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1.2" fill="#c77dff" opacity=".13"/>
    </pattern>
  </defs>

  <rect width="{W}" height="{H}" rx="18" fill="url(#fundo)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#grade)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#halo)"/>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" fill="none" stroke="#7b2cbf" stroke-opacity=".38"/>

  <g opacity=".85">
    <rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="12" fill="#0f0021" fill-opacity=".72" stroke="#7b2cbf" stroke-opacity=".45"/>
    <circle cx="{tx+22}" cy="{ty+24}" r="5" fill="#c77dff" opacity=".9"/>
    <circle cx="{tx+40}" cy="{ty+24}" r="5" fill="#7b2cbf" opacity=".8"/>
    <circle cx="{tx+58}" cy="{ty+24}" r="5" fill="#5a189a" opacity=".8"/>
    <path d="M{tx} {ty+38}h{tw}" stroke="#7b2cbf" stroke-opacity=".3"/>
    {codigo}
  </g>

  {texto("lucas@github:~$ whoami", 64, 76, 15, "#9d4edd", ls=.6)}
  {texto("LUCAS CHACON", 62, 138, 44, "#ffffff", ls=4.5, peso="bold")}
  <rect x="64" y="158" width="150" height="3" rx="1.5" fill="url(#risco)"/>
  {texto("full stack developer · pós em cibersegurança", 64, 190, 15.5, "#c77dff", ls=.4)}
  {texto("Rio de Janeiro, BR  ·  react · next · fastapi · php · postgres", 64, 216, 12.5, "#9d8bb5", ls=.3)}
</svg>
'''
open(os.path.join(OUT, "hero.svg"), "w", encoding="utf-8").write(hero)
print(f"hero.svg  {W}x{H}")

# --- rodape ----------------------------------------------------------------
# fundo transparente de proposito: funciona no tema claro e no escuro do GitHub.
FW, FH = 1000, 74
frase = "a segurança é um processo, não um produto"
rodape = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{FW}" height="{FH}" viewBox="0 0 {FW} {FH}" role="img" aria-label="{frase}">
  <title>{frase}</title>
  <defs>
    <linearGradient id="fio" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#7b2cbf" stop-opacity="0"/>
      <stop offset=".5" stop-color="#c77dff" stop-opacity=".9"/>
      <stop offset="1" stop-color="#7b2cbf" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="0" y="16" width="{FW}" height="1.5" fill="url(#fio)"/>
  <circle cx="{FW/2}" cy="16.75" r="3.5" fill="#c77dff"/>
  {texto(frase, FW/2, 54, 14, "#8b7aa8", ls=.8, anchor="middle")}
</svg>
'''
open(os.path.join(OUT, "rodape.svg"), "w", encoding="utf-8").write(rodape)
print(f"rodape.svg  {FW}x{FH}")
