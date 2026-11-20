# -*- coding: utf-8 -*-
"""Gera o cartao da stack por camada (assets/social/camadas.svg).

Regra de cor da pagina: texto em neutro, roxo so onde marca hierarquia
(prompt, rotulo de camada, borda). Roxo em tudo vira uniforme, nao identidade.
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "assets", "social")
MONO = "DejaVu Sans Mono,Menlo,Consolas,Liberation Mono,monospace"

ROTULO, TEXTO, PONT, CMD = "#c77dff", "#e6edf3", "#7b2cbf", "#ffffff"

IDIOMAS = {
    "pt": dict(saida=os.path.join(OUT, "camadas.svg"), titulo="stack por camada",
               comando="stack --por-camada", camadas=[
        ("front-end",  "React · Next.js · TypeScript · React Native (Expo) · Vite · Tailwind · Bootstrap · jQuery"),
        ("estado",     "Redux Toolkit · React Hook Form · Zod · Yup"),
        ("back-end",   "NestJS · Node.js / Express · PHP 8 · Python (FastAPI)"),
        ("dados",      "PostgreSQL · Prisma · Redis · MySQL · MariaDB · SQLite · SQLAlchemy · Drizzle"),
        ("testes",     "Vitest · Playwright · Pytest"),
        ("segurança",  "JWT · bcrypt · NextAuth · Kali Linux · pentest · auditoria e logs"),
        ("integrações","MercadoPago · Uber Direct · Telegram API · OpenAI · Groq · PHPMailer · QR Code"),
        ("infra",      "Docker · Caddy · VPS (CI e deploy próprios) · Cloudflare R2 · Render · Vercel"),
        ("ia",         "Claude Code (multiagentes)"),
    ]),
    "en": dict(saida=os.path.join(OUT, "en", "camadas.svg"), titulo="stack by layer",
               comando="stack --by-layer", camadas=[
        ("front-end",    "React · Next.js · TypeScript · React Native (Expo) · Vite · Tailwind · Bootstrap · jQuery"),
        ("state",        "Redux Toolkit · React Hook Form · Zod · Yup"),
        ("back-end",     "NestJS · Node.js / Express · PHP 8 · Python (FastAPI)"),
        ("data",         "PostgreSQL · Prisma · Redis · MySQL · MariaDB · SQLite · SQLAlchemy · Drizzle"),
        ("testing",      "Vitest · Playwright · Pytest"),
        ("security",     "JWT · bcrypt · NextAuth · Kali Linux · pentest · auditing and logs"),
        ("integrations", "MercadoPago · Uber Direct · Telegram API · OpenAI · Groq · PHPMailer · QR Code"),
        ("infra",        "Docker · Caddy · VPS (in-house CI and deploy) · Cloudflare R2 · Render · Vercel"),
        ("ai",           "Claude Code (multi-agent)"),
    ]),
}

FS, LH, PAD, W = 12.5, 23.0, 30.0, 900

def gerar(saida, titulo, comando, camadas):
    larg_rot = max(len(c) for c, _ in camadas)

    linhas, y = [], PAD + 34
    for nome, ferramentas in camadas:
        pontos = "." * (larg_rot + 2 - len(nome))
        linhas.append(
            f'<text x="{PAD}" y="{y:.0f}" font-family="{MONO}" font-size="{FS}" xml:space="preserve">'
            f'<tspan fill="{ROTULO}">{nome} </tspan><tspan fill="{PONT}">{pontos}</tspan>'
            f'<tspan fill="{TEXTO}"> {ferramentas}</tspan></text>')
        y += LH
    H = int(y + PAD - 8)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{titulo}">
      <title>{titulo}</title>
      <defs><linearGradient id="fundo_cam" x1="0" y1="0" x2=".7" y2="1">
        <stop offset="0" stop-color="#191526"/><stop offset="1" stop-color="#14111e"/>
      </linearGradient></defs>
      <rect width="{W}" height="{H}" rx="14" fill="url(#fundo_cam)"/>
      <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="13.25" fill="none" stroke="#3d2b5c"/>
      <text x="{PAD}" y="{PAD + 12}" font-family="{MONO}" font-size="14" xml:space="preserve"><tspan fill="{PONT}">└─$ </tspan><tspan fill="{CMD}">{comando}</tspan></text>
      {"".join(linhas)}
    </svg>
    '''
    open(saida, "w", encoding="utf-8").write(svg)
    print(f"{saida}  {W}x{H}")


for cfg in IDIOMAS.values():
    gerar(**cfg)
