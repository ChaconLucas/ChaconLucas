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


# --- animacao --------------------------------------------------------------
# SMIL roda dentro de <img> no GitHub (e o mesmo mecanismo da cobrinha).

ESTRELAS = """<circle cx="355" cy="56" r="1.3" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="2.5s" begin="3.3s" repeatCount="indefinite"/></circle>
  <circle cx="120" cy="111" r="1.5" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="4.9s" begin="0.9s" repeatCount="indefinite"/></circle>
  <circle cx="112" cy="129" r="1.3" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.1s" begin="2.2s" repeatCount="indefinite"/></circle>
  <circle cx="84" cy="229" r="1.5" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="5.1s" begin="2.5s" repeatCount="indefinite"/></circle>
  <circle cx="620" cy="33" r="1.5" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.5s" begin="3.9s" repeatCount="indefinite"/></circle>
  <circle cx="71" cy="160" r="1.8" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.2s" begin="0.6s" repeatCount="indefinite"/></circle>
  <circle cx="144" cy="164" r="1.2" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="4.7s" begin="0.7s" repeatCount="indefinite"/></circle>
  <circle cx="405" cy="42" r="1.4" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="2.6s" begin="0.2s" repeatCount="indefinite"/></circle>
  <circle cx="234" cy="145" r="1.6" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.6s" begin="1.3s" repeatCount="indefinite"/></circle>
  <circle cx="394" cy="94" r="1.1" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="2.9s" begin="3.1s" repeatCount="indefinite"/></circle>
  <circle cx="107" cy="165" r="1.2" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.8s" begin="1.4s" repeatCount="indefinite"/></circle>
  <circle cx="483" cy="91" r="1.5" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="2.6s" begin="2.0s" repeatCount="indefinite"/></circle>
  <circle cx="192" cy="211" r="1.2" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="5.0s" begin="1.7s" repeatCount="indefinite"/></circle>
  <circle cx="708" cy="37" r="1.7" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="4.0s" begin="3.5s" repeatCount="indefinite"/></circle>
  <circle cx="345" cy="105" r="1.6" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="4.1s" begin="2.3s" repeatCount="indefinite"/></circle>
  <circle cx="491" cy="35" r="1.7" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="5.0s" begin="1.9s" repeatCount="indefinite"/></circle>
  <circle cx="704" cy="34" r="1.0" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="4.4s" begin="2.6s" repeatCount="indefinite"/></circle>
  <circle cx="721" cy="228" r="1.3" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="4.4s" begin="3.5s" repeatCount="indefinite"/></circle>
  <circle cx="379" cy="23" r="1.8" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.4s" begin="2.4s" repeatCount="indefinite"/></circle>
  <circle cx="529" cy="33" r="1.1" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.2s" begin="3.0s" repeatCount="indefinite"/></circle>
  <circle cx="431" cy="118" r="1.8" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="3.8s" begin="0.7s" repeatCount="indefinite"/></circle>
  <circle cx="435" cy="158" r="1.2" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="2.8s" begin="1.7s" repeatCount="indefinite"/></circle>
  <circle cx="587" cy="89" r="1.6" fill="#c77dff" opacity=".15"><animate attributeName="opacity" values=".12;.85;.12" dur="5.2s" begin="2.7s" repeatCount="indefinite"/></circle>"""

FRASES = [
    "full stack developer · react · python · php",
    "pós-graduando em cibersegurança",
    "construindo plataformas de ponta a ponta",
    "do banco de dados ao deploy",
]

def frases_ciclando(x, y, fs, cor, ls, ciclo=15.2):
    """Cada frase acende no seu turno e apaga — o texto que se digitava sozinho,
    agora sem depender de servico externo."""
    fatia = ciclo / len(FRASES)
    fade = 0.35 / ciclo
    saida = []
    for i, f in enumerate(FRASES):
        ini, fim = i * fatia / ciclo, (i * fatia + fatia) / ciclo
        kt = [0, max(ini, .001), min(ini + fade, fim), max(fim - fade, ini + fade), fim, 1]
        kt = sorted(set(round(k, 4) for k in kt))
        vals = ["0", "0", "1", "1", "0", "0"][:len(kt)]
        w = mono_w(f, fs, ls)
        saida.append(
            f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{fs}" letter-spacing="{ls}" '
            f'fill="{cor}" textLength="{w:.1f}" lengthAdjust="spacing" opacity="{1 if i == 0 else 0}">{f}'
            f'<animate attributeName="opacity" dur="{ciclo}s" repeatCount="indefinite" '
            f'keyTimes="{";".join(str(k) for k in kt)}" values="{";".join(vals)}"/></text>')
    return "\n  ".join(saida)

# --- hero ------------------------------------------------------------------
W, H = 1000, 250

# janelinha de terminal decorativa no canto direito
tx, ty, tw, th = 612, 54, 330, 142
barras = [(196, "#7b2cbf", .95), (128, "#c77dff", .55), (238, "#5a189a", .9),
          (96, "#c77dff", .35), (168, "#7b2cbf", .7)]
codigo = "".join(
    f'<rect x="{tx+20}" y="{ty+52+i*17}" width="{lw}" height="7" rx="3.5" fill="{c}" opacity="{o}">'
    f'<animate attributeName="width" from="0" to="{lw}" dur="0.5s" begin="{0.7+i*0.3:.1f}s" fill="freeze"/></rect>'
    for i, (lw, c, o) in enumerate(barras))
# cursor piscando no fim do bloco de codigo
codigo += (f'<rect x="{tx+20}" y="{ty+52+len(barras)*17}" width="9" height="7" rx="2" fill="#c77dff" opacity="0">'
           f'<animate attributeName="opacity" values="0;0;.9;.9;0" keyTimes="0;.49;.5;.99;1" dur="1.1s" '
           f'begin="{0.7+len(barras)*0.3:.1f}s" repeatCount="indefinite"/></rect>')

lp = mono_w("lucas@github:~$ whoami", 15, .6)

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
  <rect width="{W}" height="{H}" rx="18" fill="url(#halo)" opacity=".8">
    <animate attributeName="opacity" values=".62;1;.62" dur="7s" repeatCount="indefinite"/></rect>
  {ESTRELAS}
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" fill="none" stroke="#7b2cbf" stroke-opacity=".38"/>

  <g opacity=".85">
    <rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="12" fill="#0f0021" fill-opacity=".72" stroke="#7b2cbf" stroke-opacity=".45"/>
    <circle cx="{tx+22}" cy="{ty+24}" r="5" fill="#c77dff" opacity=".9"/>
    <circle cx="{tx+40}" cy="{ty+24}" r="5" fill="#7b2cbf" opacity=".8"/>
    <circle cx="{tx+58}" cy="{ty+24}" r="5" fill="#5a189a" opacity=".8"/>
    <path d="M{tx} {ty+38}h{tw}" stroke="#7b2cbf" stroke-opacity=".3"/>
    {codigo}
  </g>

  <clipPath id="digitando"><rect x="64" y="58" width="{lp:.1f}" height="26">
    <animate attributeName="width" from="0" to="{lp:.1f}" dur="1.5s" fill="freeze"/></rect></clipPath>
  <g clip-path="url(#digitando)">{texto("lucas@github:~$ whoami", 64, 76, 15, "#9d4edd", ls=.6)}</g>
  <rect x="{64+lp+4:.1f}" y="63" width="9" height="16" fill="#c77dff" opacity="0">
    <animate attributeName="opacity" values=".9;.9;0;0" keyTimes="0;.49;.5;1" dur="1.1s" begin="1.55s" repeatCount="indefinite"/></rect>
  {texto("LUCAS CHACON", 62, 138, 44, "#ffffff", ls=4.5, peso="bold")}
  <rect x="64" y="158" width="150" height="3" rx="1.5" fill="url(#risco)">
    <animate attributeName="width" from="0" to="150" dur="1.1s" begin="1.4s" fill="freeze"/></rect>
  {frases_ciclando(64, 190, 14.5, "#c77dff", .4)}
  {texto("Rio de Janeiro, BR  ·  remoto ou híbrido", 64, 216, 12.5, "#9d8bb5", ls=.3)}
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
