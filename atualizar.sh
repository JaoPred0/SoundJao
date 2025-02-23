#!/bin/bash

# Configuração das cores
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)
CYAN=$(tput setaf 6)
RESET=$(tput sgr0)

# Definição das variáveis
PASTA_PROJETO="$HOME/SoundJao"
REPO_URL="https://github.com/JaoPred0/SoundJao.git"
SCRIPT_INICIAL="termux.py"

echo "${CYAN}🔄 Atualizando SoundJao...${RESET}"
sleep 1

# Verifica se o Git está instalado
if ! command -v git &> /dev/null; then
    echo "${RED}❌ Git não encontrado! Instale o Git antes de continuar.${RESET}"
    exit 1
fi

# Remove a pasta do projeto, se existir
if [ -d "$PASTA_PROJETO" ]; then
    echo "${YELLOW}🗑️ Removendo versão antiga...${RESET}"
    rm -rf "$PASTA_PROJETO"
    sleep 1
fi

# Clona novamente o repositório
echo "${CYAN}📥 Baixando nova versão...${RESET}"
git clone "$REPO_URL" "$PASTA_PROJETO" &> /dev/null

# Verifica se o clone foi bem-sucedido
if [ -d "$PASTA_PROJETO" ]; then
    echo "${GREEN}✅ Atualização concluída com sucesso!${RESET}"
    
    # Barra de progresso falsa
    for i in {1..5}; do
        echo -n "🔄 Processando atualização ["
        for j in $(seq 1 $i); do echo -n "■"; done
        for j in $(seq $i 5); do echo -n " "; done
        echo -n "]"
        echo -e "\r\c"
        sleep 0.5
    done
    echo ""

    # Entra no diretório e inicia o script
    cd "$PASTA_PROJETO" || exit
    echo "${CYAN}🚀 Iniciando $SCRIPT_INICIAL...${RESET}"
    sleep 2
    python3 "$SCRIPT_INICIAL"
else
    echo "${RED}❌ Falha ao atualizar o repositório.${RESET}"
    exit 1
fi
