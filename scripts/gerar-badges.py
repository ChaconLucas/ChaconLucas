# -*- coding: utf-8 -*-
"""Gera os badges do topo do README como SVG proprio (assets/social/).

Rode `python3 scripts/gerar-badges.py` depois de mexer em cor, texto ou tamanho.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")

# --- medidas ---------------------------------------------------------------
PILL_H = 32.0          # altura da pilula
MARGEM = 5.0           # folga em volta, pra sombra nao ser cortada
FS, LS = 11.5, 1.35    # fonte e espacamento entre letras
ICON = 14.0
PAD_L, GAP, PAD_R = 13.0, 8.0, 15.0

# larguras aproximadas (em) da Verdana Bold em caixa alta
W = {'A':.78,'B':.72,'C':.74,'D':.77,'E':.68,'F':.63,'G':.81,'H':.78,'I':.37,'J':.55,
     'K':.76,'L':.63,'M':.89,'N':.76,'O':.84,'P':.68,'Q':.84,'R':.74,'S':.70,'T':.66,
     'U':.76,'V':.74,'W':1.05,'X':.74,'Y':.70,'Z':.68,'Ó':.84,'É':.68,'Á':.78,' ':.34,
     '-':.43,'·':.34,'.':.34}

def largura_texto(t):
    return sum(W.get(c, .75) for c in t) * FS + LS * (len(t) - 1)

# --- icones (viewBox 24) ---------------------------------------------------
GLOBO = ('<g fill="none" stroke="{c}" stroke-width="2.1" stroke-linecap="round">'
         '<circle cx="12" cy="12" r="9.1"/><path d="M2.9 12h18.2"/>'
         '<path d="M12 2.9c2.5 2.6 3.8 5.7 3.8 9.1s-1.3 6.5-3.8 9.1c-2.5-2.6-3.8-5.7-3.8-9.1S9.5 5.5 12 2.9z"/></g>')
CARTA = ('<g fill="none" stroke="{c}" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round">'
         '<rect x="2.4" y="5" width="19.2" height="14" rx="2.6"/><path d="M3.4 6.7L12 13l8.6-6.3"/></g>')
LINKEDIN = ('<path fill="{c}" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 '
            '2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 '
            '7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 '
            '2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 '
            '24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>')
GITHUB = ('<path fill="{c}" d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 '
          '0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 '
          '1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 '
          '0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 '
          '2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 '
          '1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>')

SETA = ('<g fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M7 17L17 7"/><path d="M8.5 7H17v8.5"/></g>')
CADEADO = ('<g fill="none" stroke="{c}" stroke-width="2.1" stroke-linejoin="round">'
           '<rect x="4.2" y="10.4" width="15.6" height="10.4" rx="2.4"/>'
           '<path d="M8 10.4V7.6a4 4 0 018 0v2.8"/></g>')


def badge(nome, rotulo, icone, g1, g2, fg, borda, sombra, brilho):
    """Uma pilula com quatro camadas de profundidade: sombra projetada,
    gradiente de base, brilho no topo e fio de borda."""
    tw = largura_texto(rotulo)
    pw = PAD_L + ICON + GAP + tw + PAD_R          # largura da pilula
    W_, H_ = pw + MARGEM * 2, PILL_H + MARGEM * 2  # canvas com folga
    x0, y0 = MARGEM, MARGEM
    r = PILL_H / 2
    tx = x0 + PAD_L + ICON + GAP
    cy = y0 + PILL_H / 2
    uid = nome.replace("-", "_")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W_:.0f}" height="{H_:.0f}" viewBox="0 0 {W_:.1f} {H_:.1f}" role="img" aria-label="{rotulo}">
  <title>{rotulo}</title>
  <defs>
    <linearGradient id="base_{uid}" x1="0" y1="0" x2=".35" y2="1">
      <stop offset="0" stop-color="{g1}"/><stop offset="1" stop-color="{g2}"/>
    </linearGradient>
    <linearGradient id="luz_{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="{brilho}"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <filter id="sombra_{uid}" x="-25%" y="-40%" width="150%" height="200%">
      <feDropShadow dx="0" dy="1.6" stdDeviation="{sombra[1]}" flood-color="{sombra[0]}" flood-opacity="{sombra[2]}"/>
    </filter>
  </defs>
  <g filter="url(#sombra_{uid})">
    <rect x="{x0}" y="{y0}" width="{pw:.1f}" height="{PILL_H}" rx="{r}" fill="url(#base_{uid})"/>
  </g>
  <rect x="{x0+.6}" y="{y0+.6}" width="{pw-1.2:.1f}" height="{PILL_H/2:.1f}" rx="{r-.6:.1f}" fill="url(#luz_{uid})"/>
  <rect x="{x0+.5}" y="{y0+.5}" width="{pw-1:.1f}" height="{PILL_H-1}" rx="{r-.5:.1f}" fill="none" stroke="{borda}" stroke-width="1"/>
  <g transform="translate({x0+PAD_L:.1f},{cy-ICON/2:.1f}) scale({ICON/24:.4f})">{icone.format(c=fg)}</g>
  <text x="{tx:.1f}" y="{cy:.1f}" dy=".34em" textLength="{tw:.1f}" lengthAdjust="spacing"
        font-family="Verdana,DejaVu Sans,Geneva,sans-serif" font-size="{FS}" font-weight="bold"
        letter-spacing="{LS}" fill="{fg}">{rotulo}</text>
</svg>
'''
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, nome + ".svg"), "w", encoding="utf-8").write(svg)
    print(f"{nome}.svg  {W_:.0f}x{H_:.0f}")


# destaque: gradiente claro + halo roxo. secundarios: escuros, sombra neutra.
# acao principal: unico elemento que recebe o gradiente roxo -> rosa
badge("portfolio", "PORTFÓLIO",    GLOBO,    "#c77dff", "#ff79c6", "#ffffff",
      borda="#ffffff40", sombra=("#d95fd0", 3.6, .6), brilho=.24)
badge("linkedin",  "LINKEDIN",     LINKEDIN, "#3c096c", "#240046", "#e0c3fc",
      borda="#7b2cbf88", sombra=("#000000", 2.4, .45), brilho=.09)
badge("email",     "E-MAIL",       CARTA,    "#3c096c", "#240046", "#e0c3fc",
      borda="#7b2cbf88", sombra=("#000000", 2.4, .45), brilho=.09)
badge("repos",     "REPOSITÓRIOS", GITHUB,   "#3c096c", "#240046", "#e0c3fc",
      borda="#7b2cbf88", sombra=("#000000", 2.4, .45), brilho=.09)


# --- botoes de acao dos cards de projeto -----------------------------------
# mesma linguagem das pilulas do topo, em escala menor: sao acao secundaria.
PILL_H, FS, LS, ICON = 24.0, 9.5, 1.1, 11.5
PAD_L, GAP, PAD_R = 10.0, 6.0, 12.0

badge("btn-demo",    "VER DEMO",      SETA,    "#5a189a", "#3c096c", "#efe0ff",
      borda="#9d4edd99", sombra=("#000000", 2.0, .42), brilho=.10)
badge("btn-loja",    "VER A LOJA",    SETA,    "#5a189a", "#3c096c", "#efe0ff",
      borda="#9d4edd99", sombra=("#000000", 2.0, .42), brilho=.10)
badge("btn-codigo",  "CÓDIGO",        GITHUB,  "#5a189a", "#3c096c", "#efe0ff",
      borda="#9d4edd99", sombra=("#000000", 2.0, .42), brilho=.10)
badge("btn-privado", "REPO PRIVADO",  CADEADO, "#1c0733", "#140525", "#8f6bb8",
      borda="#4a2472aa", sombra=("#000000", 1.6, .30), brilho=.05)
