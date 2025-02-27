import sys
import pyfiglet
from colorama import Fore, Style
from config import configurar, CONFIG, limpar_terminal
from download import baixar_musica

VERSAO = "3.2"

def mostrar_banner():
    """Exibe o banner do SoundJao"""
    limpar_terminal()
    banner = pyfiglet.figlet_format("SoundJao")
    print(Fore.MAGENTA + banner + Style.RESET_ALL)
    print(Fore.CYAN + f"Downloader de músicas - Versão {VERSAO}" + Style.RESET_ALL)
    print("=" * 40)

if __name__ == "__main__":
    while True:
        mostrar_banner()
        print(Fore.YELLOW + "1 - Baixar música" + Style.RESET_ALL)
        print(Fore.YELLOW + "2 - Configurações" + Style.RESET_ALL)
        print(Fore.YELLOW + "3 - Sair" + Style.RESET_ALL)
        
        opcao = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL).strip()
        
        if opcao == "1":
            url = input(Fore.CYAN + "Digite a URL do SoundCloud: " + Style.RESET_ALL).strip()
            if url:
                baixar_musica(url)
        elif opcao == "2":
            configurar()
        elif opcao == "3":
            print(Fore.RED + "Saindo..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opção inválida, tente novamente!" + Style.RESET_ALL)
