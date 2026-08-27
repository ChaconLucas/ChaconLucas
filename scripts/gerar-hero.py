# -*- coding: utf-8 -*-
"""Gera o hero do topo e o rodape do README (assets/social/).

Duas regras que ficaram claras na marra:

1. `textLength` so onde a largura precisa ser conhecida (texto centralizado).
   Em texto alinhado a esquerda ele nao ajuda e, se a estimativa errar, o SVG
   espreme os glifos um por cima do outro.
2. Cada atributo guarda o ESTADO FINAL e o <animate> so encena a chegada nele,
   pra quem nao roda SMIL ver a arte pronta em vez de um esqueleto vazio.

Rode `python3 scripts/gerar-hero.py` depois de mexer em texto ou cor.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
os.makedirs(OUT, exist_ok=True)

MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"
W, H = 1000, 250

def txt(t, x, y, fs, cor, ls=0.0, peso="normal", extra=""):
    """Texto solto: sem textLength, a fonte decide a largura."""
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{fs}" font-weight="{peso}" '
            f'letter-spacing="{ls}" fill="{cor}"{extra}>{t}</text>')

def txt_centrado(t, cx, y, fs, cor, ls=0.0):
    """Aqui a largura precisa ser conhecida, entao vale fixar."""
    w = len(t) * fs * 0.6 + ls * (len(t) - 1)
    return (f'<text x="{cx - w/2:.1f}" y="{y}" font-family="{MONO}" font-size="{fs}" '
            f'letter-spacing="{ls}" fill="{cor}" textLength="{w:.1f}" lengthAdjust="spacing">{t}</text>')


# --- ASCII art do nome: fonte de bloco 4x5 desenhada a mao -----------------
BLOCO = {
    "L": ["█   ", "█   ", "█   ", "█   ", "████"],
    "U": ["█  █", "█  █", "█  █", "█  █", "████"],
    "C": ["████", "█   ", "█   ", "█   ", "████"],
    "A": ["████", "█  █", "████", "█  █", "█  █"],
    "S": ["████", "█   ", "████", "   █", "████"],
    "H": ["█  █", "█  █", "████", "█  █", "█  █"],
    "O": ["████", "█  █", "█  █", "█  █", "████"],
    "N": ["█  █", "██ █", "█ ██", "█  █", "█  █"],
    " ": ["  ", "  ", "  ", "  ", "  "],
}

def ascii_art(palavra):
    """Devolve as 5 linhas da palavra em blocos."""
    return [" ".join(BLOCO[c][i] for c in palavra) for i in range(5)]

# --- fundo: estrelas cintilando (posicoes fixas, nada de sortear a cada build)
PONTOS = [(96,52,1.4,3.8,.2),(212,38,1.1,4.6,1.9),(330,64,1.5,3.1,.7),(150,204,1.2,4.2,2.6),
          (268,222,1.0,3.6,1.2),(404,196,1.3,5.0,3.1),(58,150,1.1,4.4,2.2),(352,120,1.0,3.3,1.5),
          (474,72,1.4,4.8,.4),(520,214,1.2,3.9,2.9),(430,42,1.0,4.1,1.1),(180,110,1.3,5.2,3.4),
          (556,110,1.1,3.7,2.0),(88,232,1.2,4.5,.9),(300,168,1.0,3.4,2.4),(480,148,1.3,4.9,1.6)]
ESTRELAS = "\n  ".join(
    f'<circle cx="{x}" cy="{y}" r="{r}" fill="#c77dff" opacity=".18">'
    f'<animate attributeName="opacity" values=".12;.8;.12" dur="{d}s" begin="{b}s" repeatCount="indefinite"/></circle>'
    for x, y, r, d, b in PONTOS)

# --- as quatro frases que se revezam
FRASES = ["full stack developer · react · python · php",
          "pós-graduando em cibersegurança",
          "construindo plataformas de ponta a ponta",
          "do banco de dados ao deploy"]
CICLO = 15.2

def frases_ciclando(x, y, fs, cor):
    fatia, fade = CICLO / len(FRASES), 0.35 / CICLO
    saida = []
    for i, f in enumerate(FRASES):
        ini, fim = i * fatia / CICLO, (i * fatia + fatia) / CICLO
        kt = sorted({round(k, 4) for k in (0, max(ini, .001), ini + fade, fim - fade, fim, 1)})
        vals = ["0", "0", "1", "1", "0", "0"][:len(kt)]
        anim = (f'<animate attributeName="opacity" dur="{CICLO}s" repeatCount="indefinite" '
                f'keyTimes="{";".join(str(k) for k in kt)}" values="{";".join(vals)}"/>')
        # a primeira fica visivel por padrao: e ela que aparece se o SMIL nao rodar
        saida.append(txt(f, x, y, fs, cor, ls=.4, extra=f' opacity="{1 if i == 0 else 0}"').replace("</text>", anim + "</text>"))
    return "\n  ".join(saida)

# --- janela de terminal: codigo de verdade, nao barras cinzas
JX, JY, JW, JH = 596, 40, 356, 182
LINHAS = [[("{", "#7b2cbf")],
          [('  "front"', "#c77dff"), (": ", "#7b2cbf"), ('"react · next · ts"', "#e0c3fc"), (",", "#7b2cbf")],
          [('  "back"', "#c77dff"), (":  ", "#7b2cbf"), ('"fastapi · php"', "#e0c3fc"), (",", "#7b2cbf")],
          [('  "data"', "#c77dff"), (":  ", "#7b2cbf"), ('"postgres · redis"', "#e0c3fc"), (",", "#7b2cbf")],
          [('  "sec"', "#c77dff"), (":   ", "#7b2cbf"), ('"pentest · jwt"', "#e0c3fc")],
          [("}", "#7b2cbf")]]
FS_CODE, LH = 12.5, 19.5

def linha_codigo(pedacos, i):
    y = JY + 62 + i * LH
    # tspan encadeado: cada pedaco herda a posicao do anterior
    conteudo = "".join(f'<tspan fill="{c}">{t}</tspan>' for t, c in pedacos)
    anim = (f'<animate attributeName="opacity" values="0;1" dur="0.45s" '
            f'begin="{1.1 + i * 0.22:.2f}s" fill="freeze"/>')
    return (f'<text x="{JX + 22}" y="{y}" font-family="{MONO}" font-size="{FS_CODE}" '
            f'xml:space="preserve" opacity="1">{conteudo}{anim}</text>')

CODIGO = "\n    ".join(linha_codigo(l, i) for i, l in enumerate(LINHAS))
# cursor logo depois do "}" da ultima linha, dentro da janela
CURSOR_CODE = (f'<rect x="{JX + 22 + FS_CODE * 0.6 * 2:.0f}" y="{JY + 62 + (len(LINHAS)-1) * LH - 9:.0f}" '
               f'width="8" height="12" rx="2" fill="#c77dff" opacity="0">'
               f'<animate attributeName="opacity" values="0;0;.85;.85;0" keyTimes="0;.49;.5;.99;1" '
               f'dur="1.1s" begin="{1.1 + len(LINHAS) * 0.22:.2f}s" repeatCount="indefinite"/></rect>')


# --- bloco ASCII do nome ---------------------------------------------------
NOME = "LUCAS CHACON"
ART = ascii_art(NOME)
FS_ART, LH_ART = 13.0, 13.1
ART_X, ART_Y = 56, 74
ART_W = max(len(l) for l in ART) * FS_ART * 0.6      # p/ o clip da revelacao

ARTE = "\n  ".join(
    f'<text x="{ART_X}" y="{ART_Y + i * LH_ART:.1f}" font-family="{MONO}" font-size="{FS_ART}" '
    f'fill="#ffffff" xml:space="preserve">{linha}</text>'
    for i, linha in enumerate(ART))

PROMPT = "lucas@github:~$ whoami"
LP = len(PROMPT) * 14 * 0.6 + 0.6 * (len(PROMPT) - 1)   # so pra saber onde por o cursor

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Lucas Chacon — full stack developer">
  <title>Lucas Chacon — full stack developer</title>
  <defs>
    <linearGradient id="fundo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#10002b"/><stop offset=".55" stop-color="#240046"/><stop offset="1" stop-color="#3c096c"/>
    </linearGradient>
    <radialGradient id="halo" cx=".76" cy=".2" r=".6">
      <stop offset="0" stop-color="#7b2cbf" stop-opacity=".5"/><stop offset="1" stop-color="#7b2cbf" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="risco" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#c77dff"/><stop offset="1" stop-color="#c77dff" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grade" width="26" height="26" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1.1" fill="#c77dff" opacity=".1"/>
    </pattern>
    <clipPath id="revelando">
      <rect x="{ART_X}" y="{ART_Y - 12:.0f}" width="{ART_W:.0f}" height="{5 * LH_ART + 8:.0f}">
        <animate attributeName="width" from="0" to="{ART_W:.0f}" dur="1.4s" fill="freeze"/>
      </rect>
    </clipPath>
  </defs>

  <rect width="{W}" height="{H}" rx="18" fill="url(#fundo)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#grade)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#halo)" opacity=".85">
    <animate attributeName="opacity" values=".65;1;.65" dur="7s" repeatCount="indefinite"/>
  </rect>
  {ESTRELAS}
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" fill="none" stroke="#7b2cbf" stroke-opacity=".4"/>

  <g>
    <rect x="{JX}" y="{JY}" width="{JW}" height="{JH}" rx="12" fill="#0f0021" fill-opacity=".8" stroke="#7b2cbf" stroke-opacity=".5"/>
    <circle cx="{JX+22}" cy="{JY+22}" r="4.5" fill="#c77dff" opacity=".9"/>
    <circle cx="{JX+39}" cy="{JY+22}" r="4.5" fill="#7b2cbf" opacity=".85"/>
    <circle cx="{JX+56}" cy="{JY+22}" r="4.5" fill="#5a189a" opacity=".85"/>
    {txt("stack.json", JX + 240, JY + 26, 11.5, "#8b7aa8")}
    <path d="M{JX} {JY+40}h{JW}" stroke="#7b2cbf" stroke-opacity=".35"/>
    {CODIGO}
    {CURSOR_CODE}
  </g>

  <g clip-path="url(#revelando)">
  {ARTE}
  </g>
  <rect x="{ART_X}" y="{ART_Y + 5 * LH_ART - 4:.0f}" width="{ART_W:.0f}" height="2.5" rx="1.25" fill="url(#risco)">
    <animate attributeName="width" from="0" to="{ART_W:.0f}" dur="1.1s" begin="1.3s" fill="freeze"/>
  </rect>

  {frases_ciclando(ART_X, ART_Y + 5 * LH_ART + 30, 14.5, "#c77dff")}
  {txt("Rio de Janeiro, BR  ·  remoto ou híbrido", ART_X, ART_Y + 5 * LH_ART + 54, 12.5, "#9d8bb5", ls=.3)}
</svg>
'''
open(os.path.join(OUT, "hero.svg"), "w", encoding="utf-8").write(hero)
print(f"hero.svg  {W}x{H}")

# --- rodape: fundo transparente, funciona nos dois temas do GitHub ----------
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
  <circle cx="{FW/2}" cy="16.75" r="3.5" fill="#c77dff">
    <animate attributeName="opacity" values=".45;1;.45" dur="4s" repeatCount="indefinite"/>
  </circle>
  {txt_centrado(frase, FW/2, 54, 14, "#8b7aa8", ls=.8)}
</svg>
'''
open(os.path.join(OUT, "rodape.svg"), "w", encoding="utf-8").write(rodape)
print(f"rodape.svg  {FW}x{FH}")
