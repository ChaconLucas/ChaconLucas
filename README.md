<p align="center">
  <img src="assets/social/banner.svg?v=5" alt="Lucas Chacon — full stack developer" width="100%" />
</p>

<p align="center">
  <a href="https://portfolio-delta-five-78.vercel.app"><img src="assets/social/portfolio.svg?v=5" alt="Portfólio" height="42" /></a>
  <a href="https://linkedin.com/in/lucas-chacon-129414a7"><img src="assets/social/linkedin.svg?v=5" alt="LinkedIn" height="42" /></a>
  <a href="mailto:lucaschacon79@gmail.com"><img src="assets/social/email.svg?v=5" alt="E-mail" height="42" /></a>
  <a href="https://github.com/ChaconLucas?tab=repositories"><img src="assets/social/repos.svg?v=5" alt="Repositórios" height="42" /></a>
</p>

<img src="assets/social/titulos/whoami.svg?v=5" alt="&gt;_ whoami" width="100%" />


<p align="center">
  <img src="assets/social/whoami.svg?v=5" alt="formação: Análise e Desenvolvimento de Sistemas — UNISUAM; pós: Cibersegurança (Pentest · Kali Linux); atuação: Full Stack — do banco de dados ao deploy; foco: produtos, não páginas" width="100%" />
</p>

Trabalho no ciclo completo: modelo os dados, escrevo a API, monto o front e coloco no ar —
de plataformas em FastAPI + React a e-commerces em PHP com checkout e CMS próprios,
sempre com um olhar de segurança por causa da pós.

<br>

<img src="assets/social/titulos/stack.svg?v=5" alt="&gt;_ stack" width="100%" />


<p align="center">
  <img src="assets/social/stack.svg?v=5" alt="PHP, JavaScript, TypeScript, Python, HTML, CSS, jQuery, Bootstrap, React, Next.js, Redux, Tailwind, Node.js, Express, FastAPI, MySQL, PostgreSQL, SQLite, Redis, Vite, Vitest, Git, GitHub, Figma, Linux, Kali, Bash" width="100%" />
</p>

<details>
<summary><code>>_ ver a lista completa por camada</code></summary>

<img src="assets/social/camadas.svg?v=5" alt="front-end: React, Next.js, TypeScript, React Native, Vite, Tailwind, Bootstrap, jQuery; estado: Redux Toolkit, React Hook Form, Zod, Yup; back-end: PHP 8, Node.js, Express, Python, FastAPI; dados: MySQL, PostgreSQL, MariaDB, SQLite, Redis, SQLAlchemy, Drizzle, Alembic; testes: Vitest, Playwright, Pytest; segurança: JWT, bcrypt, NextAuth, Kali Linux, pentest; integrações: MercadoPago, Uber Direct, Telegram API, OpenAI, Groq, PHPMailer, QR Code; infra: Git, monorepo, Render, Vercel, GitHub Actions" width="100%" />

</details>

<br>

<img src="assets/social/titulos/metricas.svg?v=5" alt="&gt;_ métricas" width="100%" />


<p align="center">
  <img src="assets/social/linguagens.svg?v=5" alt="Linguagens: PHP 59,4%, TypeScript 14%, Python 13,4%, CSS 4,5%, HTML 4%, JavaScript 3%" width="100%" />
</p>
</p>

<br>

<img src="assets/social/titulos/contribuicoes.svg?v=5" alt="&gt;_ contribuições" width="100%" />


<p align="center">
  <img src="assets/social/contribuicoes.svg?v=5" alt="9528 contribuições entre agosto de 2025 e agosto de 2026" width="100%" />
</p>

<br>

<img src="assets/social/titulos/experiencia.svg?v=5" alt="&gt;_ experiência" width="100%" />


<table>
  <tr>
    <td width="50%" valign="top">

### TIIX
**Full Stack Developer** &nbsp;·&nbsp; `2026 — atual`

<img src="assets/social/chips/php.svg?v=5" alt="PHP" height="28" /> <img src="assets/social/chips/javascript.svg?v=5" alt="JavaScript" height="28" /> <img src="assets/social/chips/jquery.svg?v=5" alt="jQuery" height="28" /> <img src="assets/social/chips/mysql.svg?v=5" alt="MySQL" height="28" /> <img src="assets/social/chips/bootstrap.svg?v=5" alt="Bootstrap" height="28" />

Ponta a ponta dentro do sistema: **consultas e procedures em SQL**, **APIs
REST/JSON** com seus endpoints, e as telas que consomem esses dados — tabelas,
filtros, formulários e gráficos em Bootstrap + jQuery. Também **integrações
OAuth 2.0** com APIs externas, **webhooks** e rotinas agendadas em **cron**.

</td>
<td width="50%" valign="top">

### D&Z
**Desenvolvedor Full Stack** &nbsp;·&nbsp; `nov/2025 — abr/2026`

<img src="assets/social/chips/php.svg?v=5" alt="PHP" height="28" /> <img src="assets/social/chips/javascript.svg?v=5" alt="JavaScript" height="28" /> <img src="assets/social/chips/mysql.svg?v=5" alt="MySQL" height="28" />

Painéis administrativos em PHP — sistema interno de gestão, com as telas
de cadastro, listagem e manutenção dos dados.

</td>
  </tr>
</table>

<br>

<img src="assets/social/titulos/projetos.svg?v=5" alt="&gt;_ projetos em destaque" width="100%" />


<table>
  <tr>
    <td width="50%" valign="top">

### ⚡ FLASH
<img src="assets/social/chips/typescript.svg?v=5" alt="TypeScript" height="28" /> <img src="assets/social/chips/next-js-16.svg?v=5" alt="Next.js 16" height="28" /> <img src="assets/social/chips/expo.svg?v=5" alt="Expo" height="28" /> <img src="assets/social/chips/express.svg?v=5" alt="Express" height="28" /> <img src="assets/social/chips/postgresql.svg?v=5" alt="PostgreSQL" height="28" />

Marketplace de materiais para tatuagem e body piercing com entrega rápida por motoboy.
Monorepo com quatro pacotes — `shared` (regras e design tokens), `api` (Express +
PostgreSQL), `web` (Next.js 16) e `app` (Expo / React Native) — mantendo **paridade
total entre app e web**. Integração de frete com Uber Direct e deploy contínuo na Render.

<details>
<summary><code>&gt;_ ver o monorepo</code></summary>

```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#2a0a4d','primaryTextColor':'#e0c3fc','primaryBorderColor':'#7b2cbf','lineColor':'#9d4edd','secondaryColor':'#3c096c','tertiaryColor':'#1a0033','fontFamily':'monospace'}}}%%
flowchart LR
  S[shared<br/>regras e design tokens] --> A[api<br/>Express + PostgreSQL]
  S --> W[web<br/>Next.js 16]
  S --> P[app<br/>Expo / React Native]
  A --> W
  A --> P
```

</details>

<a href="https://flash-web-srgm.onrender.com"><img src="assets/social/btn-loja.svg?v=5" alt="Ver a loja" height="34" /></a>
<img src="assets/social/btn-privado.svg?v=5" alt="Repositório privado" height="34" />

</td>
<td width="50%" valign="top">

### 🎟️ GateCheck
<img src="assets/social/chips/python.svg?v=5" alt="Python" height="28" /> <img src="assets/social/chips/fastapi.svg?v=5" alt="FastAPI" height="28" /> <img src="assets/social/chips/typescript.svg?v=5" alt="TypeScript" height="28" /> <img src="assets/social/chips/react.svg?v=5" alt="React" height="28" />

Plataforma de venda de ingressos e controle de entrada para boates e eventos.
Fluxo completo: empresa cria evento e lotes → cliente compra → pagamento confirmado
no backend → ingresso emitido com **QR Code único** → portaria valida na entrada →
tudo registrado para auditoria.

<details>
<summary><code>&gt;_ ver o fluxo</code></summary>

```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#2a0a4d','primaryTextColor':'#e0c3fc','primaryBorderColor':'#7b2cbf','lineColor':'#9d4edd','secondaryColor':'#3c096c','tertiaryColor':'#1a0033','fontFamily':'monospace'}}}%%
flowchart TD
  A[empresa cria evento e lotes] --> B[cliente compra]
  B --> C{pagamento confirmado no backend}
  C -->|aprovado| D[ingresso emitido com QR Code único]
  D --> E[portaria valida na entrada]
  E --> F[(tudo registrado para auditoria)]
```

</details>

<img src="assets/social/btn-privado.svg?v=5" alt="Repositório privado" height="34" />

</td>
  </tr>
  <tr>
    <td width="50%" valign="top">

### 🏄 WSL SporTV Games
<img src="assets/social/chips/fastapi.svg?v=5" alt="FastAPI" height="28" /> <img src="assets/social/chips/react-18.svg?v=5" alt="React 18" height="28" /> <img src="assets/social/chips/typescript.svg?v=5" alt="TypeScript" height="28" />

MVP de jogos interativos para o WSL SporTV: *Drop Sua Onda* (quiz que gera um perfil
de surfista) e *Jurado por Um Dia* (o usuário dá a nota e compara com a do juiz oficial).
Cadastro configurável antes ou depois da partida, com premiação no final.

<a href="https://wsl-sportv-games.vercel.app"><img src="assets/social/btn-demo.svg?v=5" alt="Ver demo" height="34" /></a>
<img src="assets/social/btn-privado.svg?v=5" alt="Repositório privado" height="34" />

</td>
<td width="50%" valign="top">

### 🛍️ Rare7 — E-commerce completo
<img src="assets/social/chips/php-8.svg?v=5" alt="PHP 8" height="28" /> <img src="assets/social/chips/mysql.svg?v=5" alt="MySQL" height="28" /> <img src="assets/social/chips/javascript.svg?v=5" alt="JavaScript" height="28" />

Plataforma de e-commerce que lidero tecnicamente: loja virtual, painel administrativo,
CMS integrado, checkout **MercadoPago**, automação de e-mails, dashboards com Chart.js,
chat com IA (Groq) e logs de auditoria.

<a href="https://github.com/ChaconLucas/rare7"><img src="assets/social/btn-codigo.svg?v=5" alt="Código" height="34" /></a>

</td>
  </tr>
  <tr>
    <td width="50%" valign="top">

### 🏭 Factory Production Management
<img src="assets/social/chips/fastapi.svg?v=5" alt="FastAPI" height="28" /> <img src="assets/social/chips/react.svg?v=5" alt="React" height="28" /> <img src="assets/social/chips/sqlalchemy.svg?v=5" alt="SQLAlchemy" height="28" />

Sistema full stack de gestão de produção fabril: planejamento inteligente de ordens,
controle de estoque e insights de eficiência a partir dos dados de manufatura.

<a href="https://github.com/ChaconLucas/projdata_project"><img src="assets/social/btn-codigo.svg?v=5" alt="Código" height="34" /></a>

</td>
<td width="50%" valign="top">

### 🤖 Bot da FURIA
<img src="assets/social/chips/python.svg?v=5" alt="Python" height="28" /> <img src="assets/social/chips/telegram-api.svg?v=5" alt="Telegram API" height="28" /> <img src="assets/social/chips/beautifulsoup.svg?v=5" alt="BeautifulSoup" height="28" />

Bot de Telegram para a torcida da FURIA (CS): próximos jogos, lineup atual, últimos
resultados e frases da torcida — com scraping para manter os dados atualizados.

<a href="https://github.com/ChaconLucas/furia-telegram-bot"><img src="assets/social/btn-codigo.svg?v=5" alt="Código" height="34" /></a>

</td>
  </tr>
  <tr>
    <td width="50%" valign="top">

### 🎤 Tiixokê
<img src="assets/social/chips/react.svg?v=5" alt="React" height="28" /> <img src="assets/social/chips/vite.svg?v=5" alt="Vite" height="28" /> <img src="assets/social/chips/express.svg?v=5" alt="Express" height="28" /> <img src="assets/social/chips/web-audio-api.svg?v=5" alt="Web Audio API" height="28" />

Karaokê web: busca a música no YouTube, toca o vídeo com a letra e **pontua você de
0 a 100** analisando volume e variedade de pitch captados pelo microfone em tempo real,
com animação de suspense na revelação da nota.

<img src="assets/social/btn-privado.svg?v=5" alt="Repositório privado" height="34" />

</td>
<td width="50%" valign="top">

### 📱 Gestão de Clientes e Produtos
<img src="assets/social/chips/react-native.svg?v=5" alt="React Native" height="28" /> <img src="assets/social/chips/expo.svg?v=5" alt="Expo" height="28" /> <img src="assets/social/chips/sqlite.svg?v=5" alt="SQLite" height="28" /> <img src="assets/social/chips/drizzle.svg?v=5" alt="Drizzle" height="28" />

App mobile com banco local, Redux Toolkit, React Hook Form + Yup e Expo Router —
CRUD de clientes e produtos com vínculos entre eles.

<a href="https://github.com/ChaconLucas/react_native_target"><img src="assets/social/btn-codigo.svg?v=5" alt="Código" height="34" /></a>

</td>
  </tr>
  <tr>
    <td width="50%" valign="top">

### 🧠 AIpply
`JavaScript` `Python`

Automação de candidaturas com apoio de IA — leitura de vaga, adequação do perfil e
geração do material de aplicação.

<img src="assets/social/btn-privado.svg?v=5" alt="Repositório privado" height="34" />

</td>
<td width="50%" valign="top">

### ⌚ Integrações de wearables
<img src="assets/social/chips/php.svg?v=5" alt="PHP" height="28" /> <img src="assets/social/chips/oauth-2-0.svg?v=5" alt="OAuth 2.0" height="28" /> <img src="assets/social/chips/rest.svg?v=5" alt="REST" height="28" />

Integração com múltiplas plataformas de wearables e APIs de saúde: fluxo de
autorização, troca e renovação de token, callback e sessão por provedor,
com dashboard para os dados de cada um.

`🏢 trabalho da TIIX`

</td>
  </tr>
</table>

<br>

<img src="assets/social/titulos/contato.svg?v=5" alt="&gt;_ contato" width="100%" />


```bash
$ ./contato.sh
[+] portfolio .. portfolio-delta-five-78.vercel.app
[+] linkedin ... linkedin.com/in/lucas-chacon-129414a7
[+] e-mail ..... lucaschacon79@gmail.com
[+] local ...... Rio de Janeiro — BR (remoto ou híbrido)
```

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=ChaconLucas&color=7b2cbf&style=flat-square&label=visitas+no+perfil" />
</p>

<p align="center">
  <img src="assets/social/rodape.svg?v=5" alt="a segurança é um processo, não um produto" width="100%" />
</p>
