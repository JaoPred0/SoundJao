import os
from colorama import Fore, Style

# Configuração padrão
CONFIG = {
    "download_dir": "downloads",
    "quality": "high",  # 'high' ou 'low'
    "download_playlist": True,  # Baixar playlists inteiras?
    "save_cover": True  # Salvar com capa?
}

# Criar pasta de downloads se não existir
os.makedirs(CONFIG["download_dir"], exist_ok=True)

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def configurar():
    """Menu de configuração"""
    global CONFIG
    
    while True:
        limpar_terminal()
        print(Fore.CYAN + "\n=== Configurações ===" + Style.RESET_ALL)
        print(f"1 - Diretório de download: {Fore.YELLOW}{CONFIG['download_dir']}{Style.RESET_ALL}")
        print(f"2 - Qualidade do áudio: {Fore.YELLOW}{'Alta' if CONFIG['quality'] == 'high' else 'Baixa'}{Style.RESET_ALL}")
        print(f"3 - Baixar playlists inteiras: {Fore.YELLOW}{'Sim' if CONFIG['download_playlist'] else 'Não'}{Style.RESET_ALL}")
        print(f"4 - Salvar com capa: {Fore.YELLOW}{'Sim' if CONFIG['save_cover'] else 'Não'}{Style.RESET_ALL}")
        print("5 - Salvar e voltar")

        escolha = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL).strip()
        
        if escolha == "1":
            novo_dir = input("Digite o novo diretório de download: ").strip()
            if novo_dir:
                CONFIG["download_dir"] = novo_dir
                os.makedirs(novo_dir, exist_ok=True)
        
        elif escolha == "2":
            nova_qualidade = input("Escolha a qualidade (1 - Alta, 2 - Baixa): ").strip()
            CONFIG["quality"] = "high" if nova_qualidade == "1" else "low"
        
        elif escolha == "3":
            resposta = input("Baixar playlists inteiras? (1 - Sim, 2 - Não): ").strip()
            CONFIG["download_playlist"] = resposta == "1"
        
        elif escolha == "4":
            resposta = input("Salvar com capa? (1 - Sim, 2 - Não): ").strip()
            CONFIG["save_cover"] = resposta == "1"
        
        elif escolha == "5":
            print(Fore.GREEN + "Configurações salvas!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Opção inválida! Tente novamente." + Style.RESET_ALL)
