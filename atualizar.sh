#!/bin/bash

# Configuração das cores
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)
CYAN=$(tput setaf 6)
RESET=$(tput sgr0)

# Nome do script que será salvo na raiz do Termux
SCRIPT_ATUALIZANDO="$HOME/atualizando.sh"

echo "${CYAN}🔄 Iniciando processo de atualização...${RESET}"
sleep 1

# Para o script termux.py rodando
echo "${YELLOW}🛑 Parando o script termux.py...${RESET}"
pkill -f termux.py 2>/dev/null

# Cria o script atualizando.sh na raiz do Termux
cat <<EOL > "$SCRIPT_ATUALIZANDO"
#!/bin/bash

# Configuração das cores
GREEN=\$(tput setaf 2)
YELLOW=\$(tput setaf 3)
RED=\$(tput setaf 1)
CYAN=\$(tput setaf 6)
RESET=\$(tput sgr0)

PASTA_PROJETO="\$HOME/SoundJao"
REPO_URL="https://github.com/JaoPred0/SoundJao.git"
SCRIPT_INICIAL="termux.py"

echo "\${CYAN}🗑️ Removendo versão antiga...${RESET}"
rm -rf "\$PASTA_PROJETO"

echo "\${CYAN}📥 Baixando nova versão...${RESET}"
git clone "\$REPO_URL" "\$PASTA_PROJETO" &>/dev/null

if [ -d "\$PASTA_PROJETO" ]; then
    echo "\${GREEN}✅ Atualização concluída!${RESET}"
    cd "\$PASTA_PROJETO" || exit
    echo "\${CYAN}🚀 Iniciando \$SCRIPT_INICIAL...${RESET}"
    sleep 2
    python "\$SCRIPT_INICIAL"
else
    echo "\${RED}❌ Falha ao baixar atualização.${RESET}"
fi

# Remove o próprio script após a execução
echo "\${YELLOW}🗑️ Limpando arquivos temporários...${RESET}"
rm -- "\$0"
EOL

# Dá permissão de execução ao script atualizando.sh
chmod +x "$SCRIPT_ATUALIZANDO"

# Executa o script atualizando.sh e finaliza o processo
echo "${GREEN}🚀 Iniciando atualização...${RESET}"
bash "$SCRIPT_ATUALIZANDO"
exit