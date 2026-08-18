#!/usr/bin/env bash
# Gera a animacao das contribuicoes localmente e publica na branch `output`.
# Use enquanto o GitHub Actions estiver indisponivel. Rode: bash scripts/atualizar-cobrinha.sh
set -euo pipefail

USER=ChaconLucas
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

cd "$TMP"
npm i --silent generate-snake-animation@3.5.0
node node_modules/generate-snake-animation/cli.js \
  --github_user="$USER" \
  --github_token="$(gh auth token)" \
  --output=dist/github-contribution-grid-snake.svg \
  --output='dist/github-contribution-grid-snake-dark.svg?palette=github-dark'

git clone -q --branch main "https://github.com/$USER/$USER.git" repo
cd repo
git checkout -q --orphan output
git rm -rqf .
cp ../dist/*.svg .
git add -A
git commit -q -m "Atualiza a animacao das contribuicoes"
git push -q -f origin output
echo "✅ cobrinha atualizada"
