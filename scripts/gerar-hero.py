# -*- coding: utf-8 -*-
"""Gera o hero do topo e o rodape do README (assets/social/).

O hero e um terminal: moldura de janela, prompt no estilo Kali e o nome em
ANSI Shadow (a fonte figlet dos banners de Kali e metasploit), desenhada a mao
porque nao ha figlet na maquina.

Duas regras aprendidas na marra:
1. `textLength` so onde a largura precisa ser conhecida (texto centralizado).
   Em texto alinhado a esquerda, se a estimativa errar, o SVG espreme os
   glifos um por cima do outro.
2. Cada atributo guarda o ESTADO FINAL e o <animate> so encena a chegada nele,
   pra quem nao roda SMIL ver a arte pronta em vez de um esqueleto vazio.

Rode `python3 scripts/gerar-hero.py` depois de mexer em texto ou cor.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
os.makedirs(OUT, exist_ok=True)

MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"

# --- ANSI Shadow: so as 8 letras que o nome usa ----------------------------
SHADOW = {
"L": ["██╗     ", "██║     ", "██║     ", "██║     ", "███████╗", "╚══════╝"],
"U": ["██╗   ██╗", "██║   ██║", "██║   ██║", "██║   ██║", "╚██████╔╝", " ╚═════╝ "],
"C": [" ██████╗", "██╔════╝", "██║     ", "██║     ", "╚██████╗", " ╚═════╝"],
"A": [" █████╗ ", "██╔══██╗", "███████║", "██╔══██║", "██║  ██║", "╚═╝  ╚═╝"],
"S": ["███████╗", "██╔════╝", "███████╗", "╚════██║", "███████║", "╚══════╝"],
"H": ["██╗  ██╗", "██║  ██║", "███████║", "██╔══██║", "██║  ██║", "╚═╝  ╚═╝"],
"O": [" ██████╗ ", "██╔═══██╗", "██║   ██║", "██║   ██║", "╚██████╔╝", " ╚═════╝ "],
"N": ["███╗   ██╗", "████╗  ██║", "██╔██╗ ██║", "██║╚██╗██║", "██║ ╚████║", "╚═╝  ╚═══╝"],
" ": ["   "] * 6,
}

def banner(palavra):
    return ["".join(SHADOW[c][i] for c in palavra) for i in range(6)]

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")



# --- barra de status, no rodape da janela ----------------------------------
import math

def mascote_claude(x, y, larg=22.0, cor="#c8795a", olho="#1a0a05"):
    """O mascote do Claude Code: corpo quadrado com abas laterais, olhos > <
    e quatro perninhas. Desenho proprio, em grade de 100x80."""
    e = larg / 100.0
    corpo = ("M9.5 0H90.5V16.4H100V39H90.5V80H76.5V58.8H69V80H55V58.8"
             "H45V80H31V58.8H23.5V80H9.5V39H0V16.4H9.5Z")
    return (f'<g transform="translate({x:.1f},{y:.1f}) scale({e:.4f})">'
            f'<path d="{corpo}" fill="{cor}"/>'
            f'<path d="M17.7 19.8L30.6 26L17.7 32.1" fill="none" stroke="{olho}" '
            f'stroke-width="6.5" stroke-linejoin="miter"/>'
            f'<path d="M82.3 19.8L69.4 26L82.3 32.1" fill="none" stroke="{olho}" '
            f'stroke-width="6.5" stroke-linejoin="miter"/></g>')


def barra_status(H):
    """Estilo tmux: chip da branch a esquerda, atribuicao a direita."""
    alt = 30
    y0 = H - alt
    chip_w = 54
    return f'''<path d="M0 {y0}h{W}v{alt - 14}a14 14 0 01-14 14H14a14 14 0 01-14-14z" fill="#1d0438"/>
  <path d="M0 {y0}h{W}" stroke="#7b2cbf" stroke-opacity=".3"/>
  <rect x="14" y="{y0 + 7}" width="{chip_w}" height="16" rx="4" fill="#7b2cbf"/>
  <text x="{14 + chip_w / 2}" y="{y0 + 19}" font-family="{MONO}" font-size="10.5" font-weight="bold"
        fill="#ffffff" text-anchor="middle">main</text>
  <text x="{14 + chip_w + 12}" y="{y0 + 19}" font-family="{MONO}" font-size="11"
        fill="#8b7aa8">~/lucas-chacon</text>
'''

# --- QR do portfolio -------------------------------------------------------
# Matriz assada aqui de proposito: foi gerada uma vez com o segno e colada,
# entao este script nao depende de biblioteca externa nenhuma pra rodar.
# Pra trocar a URL: segno.make(url, error="m").matrix -> 0/1 por linha.
QR_URL = "https://portfolio-delta-five-78.vercel.app"
QR = """11111110100101100110001111111
10000010111011001011101000001
10111010100011101001101011101
10111010000001001110001011101
10111010111101101011001011101
10000010010100101100001000001
11111110101010101010101111111
00000000000011110001000000000
10011111111000010100010010111
00101100010011110011000110110
00110111101111011000000110100
01000100100010000110100011001
11010110101100011001101000001
01111101001111111110001111111
00100010111011011011000000101
10010100110110010000010010101
10011111101001011000100001000
10101000011000110101100010110
11000110101101111001000001001
11100100110111111011000101100
11010011000100101100111111110
00000000110110011010100011000
11111110111010110101101011000
10000010111010001100100010000
10111010110001100011111111010
10111010110011110110010000001
10111010011010110000110110111
10000010010110010000000011101
11111110101110011011100111000"""

def qr_svg(x, y, mod=5.0):
    """Desenha o QR juntando modulos vizinhos numa mesma barra: menos elementos."""
    linhas = QR.strip().split("\n")
    barras = []
    for i, linha in enumerate(linhas):
        j = 0
        while j < len(linha):
            if linha[j] == "1":
                k = j
                while k + 1 < len(linha) and linha[k + 1] == "1":
                    k += 1
                barras.append(f'<rect x="{x + j * mod:.1f}" y="{y + i * mod:.1f}" '
                              f'width="{(k - j + 1) * mod:.1f}" height="{mod}" fill="#1a0033"/>')
                j = k + 1
            else:
                j += 1
    return "".join(barras), len(linhas) * mod

# --- medidas ---------------------------------------------------------------
W = 1000
PAD_X, TOPO = 34, 40          # respiro interno e altura da barra de titulo
FS, LH = 13.0, 19.0           # corpo do terminal
FS_ART = 10.0
LH_ART = 9.9                  # sobrepondo de leve: e o que faz as fatias virarem letra solida

COR = {"prompt": "#7b2cbf", "user": "#c77dff", "path": "#e0c3fc",
       "cmd": "#ffffff", "saida": "#9d8bb5", "chave": "#c77dff", "art": "#c77dff"}

def linha(pedacos, y, fs=FS, extra=""):
    """Uma linha de terminal montada de tspans, pra colorir por pedaco."""
    corpo = "".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in pedacos)
    return (f'<text x="{PAD_X + 14}" y="{y:.1f}" font-family="{MONO}" font-size="{fs}" '
            f'xml:space="preserve"{extra}>{corpo}</text>')

PROMPT1 = [("┌──(", COR["prompt"]), ("lucas@kali", COR["user"]), (")-[", COR["prompt"]),
           ("~", COR["path"]), ("]", COR["prompt"])]
def prompt2(cmd):
    return [("└─$ ", COR["prompt"]), (cmd, COR["cmd"])]

INFO = [("stack", "react · next · fastapi · php · postgres · redis"),
        ("segurança", "pós-graduando · pentest · kali linux"),
        ("local", "Rio de Janeiro, BR · remoto ou híbrido")]

FRASES = ["full stack developer, do banco de dados ao deploy",
          "construindo plataformas de ponta a ponta",
          "produtos, não páginas"]
CICLO = 12.6

# --- montagem do corpo -----------------------------------------------------
y = TOPO + 34
corpo, ART_Y0 = [], 0

corpo.append(linha(PROMPT1, y)); y += LH
corpo.append(linha(prompt2("whoami --banner"), y)); y += LH + 12

ART = banner("LUCAS CHACON")
ART_W = max(len(l) for l in ART) * FS_ART * 0.6
ART_Y0 = y
for i, l in enumerate(ART):
    corpo.append(f'<text x="{PAD_X + 14}" y="{y + i * LH_ART:.1f}" font-family="{MONO}" '
                 f'font-size="{FS_ART}" fill="url(#gradArt)" xml:space="preserve">{esc(l)}</text>')
y += 6 * LH_ART + 20

# frase que se reveza, no lugar de uma so estatica
fatia, fade = CICLO / len(FRASES), 0.3 / CICLO
for i, f in enumerate(FRASES):
    ini, fim = i * fatia / CICLO, (i * fatia + fatia) / CICLO
    kt = sorted({round(k, 4) for k in (0, max(ini, .001), ini + fade, fim - fade, fim, 1)})
    vals = ["0", "0", "1", "1", "0", "0"][:len(kt)]
    anim = (f'<animate attributeName="opacity" dur="{CICLO}s" repeatCount="indefinite" '
            f'keyTimes="{";".join(str(k) for k in kt)}" values="{";".join(vals)}"/>')
    corpo.append(linha([("» ", COR["prompt"]), (f, COR["saida"])], y,
                       extra=f' opacity="{1 if i == 0 else 0}"').replace("</text>", anim + "</text>"))
y += LH + 10

for chave, valor in INFO:
    pontos = "." * (16 - len(chave))
    corpo.append(linha([(f"  {chave} ", COR["chave"]), (pontos, COR["prompt"]),
                        (f" {valor}", COR["saida"])], y, fs=12.0))
    y += 17

y += 12
corpo.append(linha(PROMPT1, y)); y += LH
corpo.append(linha([("└─$ ", COR["prompt"])], y))
CURSOR_Y = y - 11

CORPO = "\n  ".join(corpo)
H = int(max(y + 46, 300))   # +46: sobra p/ a barra de status   # a janela termina onde o conteudo termina

# --- coluna da direita: o Claude Code aberto no terminal -------------------
DIV_X = 622                                  # divisoria entre as duas colunas
CX = DIV_X + 34                              # margem interna da coluna

# projetos reais, os mesmos que aparecem na secao la embaixo
PROJETOS = [("flash/", "gatecheck/"), ("rare7/", "wsl-games/"), ("tiixoke/", "aipply/")]

def painel_claude(H):
    """A coluna vira a saida de um `ls` nos projetos: conteudo real, e um
    aperitivo da secao de projetos que vem mais abaixo no README."""
    x = DIV_X + 34
    y = TOPO + 46
    l = []   # sem divisoria: o espaco entre as colunas ja separa
    l.append(f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="12.5" xml:space="preserve">'
             f'<tspan fill="#7b2cbf">┌──(</tspan><tspan fill="#c77dff">lucas@kali</tspan>'
             f'<tspan fill="#7b2cbf">)-[</tspan><tspan fill="#e0c3fc">~/projetos</tspan>'
             f'<tspan fill="#7b2cbf">]</tspan></text>')
    y += 18
    l.append(f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="12.5" xml:space="preserve">'
             f'<tspan fill="#7b2cbf">└─$ </tspan><tspan fill="#ffffff">ls</tspan></text>')
    y += 28
    for i, (esq, dir_) in enumerate(PROJETOS):
        l.append(f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="12.5" fill="#c77dff" '
                 f'xml:space="preserve" opacity="1">{esq:<13}{dir_}'
                 f'<animate attributeName="opacity" values="0;1" dur="0.35s" '
                 f'begin="{1.6 + i * 0.2:.2f}s" fill="freeze"/></text>')
        y += 19
    # o mascote ocupa a sobra abaixo da lista, em tamanho que da p/ ver
    larg = 62.0
    l.append(mascote_claude(DIV_X + (W - DIV_X) / 2 - larg / 2, y + 22, larg=larg))
    return "\n  ".join(l)

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Lucas Chacon — full stack developer">
  <title>Lucas Chacon — full stack developer</title>
  <defs>
    <linearGradient id="janela" x1="0" y1="0" x2=".6" y2="1">
      <stop offset="0" stop-color="#15012e"/><stop offset="1" stop-color="#0b0018"/>
    </linearGradient>
    <linearGradient id="barra" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2d0a52"/><stop offset="1" stop-color="#1d0438"/>
    </linearGradient>
    <linearGradient id="gradArt" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e0c3fc"/><stop offset=".5" stop-color="#c77dff"/><stop offset="1" stop-color="#7b2cbf"/>
    </linearGradient>
    <radialGradient id="brilho" cx=".5" cy="0" r=".9">
      <stop offset="0" stop-color="#7b2cbf" stop-opacity=".28"/><stop offset="1" stop-color="#7b2cbf" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="revela">
      <rect x="{PAD_X + 14}" y="{ART_Y0 - 10:.0f}" width="{ART_W:.0f}" height="{6 * LH_ART + 6:.0f}">
        <animate attributeName="width" from="0" to="{ART_W:.0f}" dur="1.6s" begin="0.9s" fill="freeze"/>
      </rect>
    </clipPath>
  </defs>

  <rect width="{W}" height="{H}" rx="14" fill="url(#janela)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#brilho)"/>
  <path d="M14 {TOPO}h{W-28}" stroke="#7b2cbf" stroke-opacity=".35"/>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="13.25" fill="none" stroke="#7b2cbf" stroke-opacity=".45"/>
  <path d="M0 14a14 14 0 0114-14h{W-28}a14 14 0 0114 14v{TOPO-14}H0z" fill="url(#barra)"/>
  <circle cx="26" cy="20" r="5" fill="#c77dff" opacity=".95"/>
  <circle cx="45" cy="20" r="5" fill="#7b2cbf" opacity=".85"/>
  <circle cx="64" cy="20" r="5" fill="#5a189a" opacity=".85"/>
  <text x="{W/2:.0f}" y="24" font-family="{MONO}" font-size="11.5" fill="#8b7aa8" text-anchor="middle">lucas@kali: ~ — zsh</text>

  <g clip-path="url(#revela)">
    {chr(10).join(l for l in CORPO.split(chr(10)) if 'gradArt' in l)}
  </g>
  {chr(10).join('  ' + l.strip() for l in CORPO.split(chr(10)) if 'gradArt' not in l)}

  {painel_claude(H)}

  {barra_status(H)}

  <rect x="{PAD_X + 14 + 4 * FS * 0.6:.0f}" y="{CURSOR_Y:.0f}" width="8" height="15" fill="#c77dff" opacity=".85">
    <animate attributeName="opacity" values=".85;.85;0;0" keyTimes="0;.49;.5;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>
</svg>
'''
open(os.path.join(OUT, "banner.svg"), "w", encoding="utf-8").write(hero)
print(f"banner.svg  {W}x{H}  (banner {ART_W:.0f}px)")

# --- rodape ----------------------------------------------------------------
FW, FH = 1000, 74
frase = "a segurança é um processo, não um produto"
lw = len(frase) * 14 * 0.6 + .8 * (len(frase) - 1)
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
  <text x="{FW/2 - lw/2:.1f}" y="54" font-family="{MONO}" font-size="14" letter-spacing=".8"
        fill="#8b7aa8" textLength="{lw:.1f}" lengthAdjust="spacing">{frase}</text>
</svg>
'''
open(os.path.join(OUT, "rodape.svg"), "w", encoding="utf-8").write(rodape)
print(f"rodape.svg  {FW}x{FH}")
