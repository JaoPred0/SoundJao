#!/bin/bash

PASTA_PROJETO="$HOME/SoundJao"
REPO_URL="https://github.com/JaoPred0/SoundJao.git"

# Verifica se há atualizações no repositório remoto
cd "$PASTA_PROJETO" || exit
git fetch

if git status | grep -q "Your branch is behind"; then
    echo "🔔 Nova atualização disponível!" > ~/update_status.txt
else
    echo "✅ SoundJao está atualizado." > ~/update_status.txt
fi
