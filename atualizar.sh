#!/bin/bash

# Parar o programa se estiver rodando
echo "🛑 Parando o programa..."
pkill -f termux.py 2>/dev/null

# Criar o arquivo atualizando.sh na pasta HOME
echo "📜 Criando script de atualização..."
cat << 'EOF' > ~/atualizando.sh
#!/bin/bash

PASTA_PROJETO="$HOME/SoundJao"
REPO_URL="https://github.com/JaoPred0/SoundJao.git"
SCRIPT_INICIAL="termux.py"

echo "🗑️ Removendo versão antiga..."
rm -rf "$PASTA_PROJETO"

echo "📥 Baixando nova versão..."
git clone "$REPO_URL" "$PASTA_PROJETO" &>/dev/null

if [ -d "$PASTA_PROJETO" ]; then
    echo "✅ Atualizado para a nova versão!" | tee ~/update_status.txt
    cd "$PASTA_PROJETO" || exit
    echo "🚀 Iniciando $SCRIPT_INICIAL..."
    python3 "$SCRIPT_INICIAL"
else
    echo "❌ Falha na atualização!" | tee ~/update_status.txt
fi

# Remover este script após a execução
rm -- "$0"
EOF

# Dar permissão de execução ao script
chmod +x ~/atualizando.sh

# Executar o script
bash ~/atualizando.sh