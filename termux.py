import os
import requests
import subprocess
import time
import re
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB
from colorama import Fore, init
import pyfiglet

# Inicializa colorama
init(autoreset=True)

# Versão do script
VERSAO = "v3.3"
SCDL_PATH = "scdl"

def limpar_terminal():
    """Limpa o terminal."""
    os.system("clear")

def exibir_banner():
    """Exibe um banner estilizado."""
    print(Fore.CYAN + pyfiglet.figlet_format("SoundJao"))
    print(Fore.YELLOW + f"Versão: {VERSAO}")
    print(Fore.GREEN + "Baixe músicas e playlists do SoundCloud!\n")

# Exibe a VPN obrigatória
def aviso_vpn():
    print(Fore.RED + "IMPORTANTE: USE UMA VPN DOS EUA PARA EVITAR ERROS NO DOWNLOAD ⚠️\n")
    time.sleep(2)

# Limpa o terminal antes de exibir o banner
limpar_terminal()
exibir_banner()

# Pergunta onde salvar
DOWNLOAD_FOLDER = input(Fore.CYAN + "Digite a pasta de download (pressione Enter para usar a pasta raiz): ").strip()
if not DOWNLOAD_FOLDER:
    DOWNLOAD_FOLDER = os.getcwd()
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def bipar():
    """Emite um alerta sonoro no Linux."""
    os.system("echo -e '\a'")

def baixar_playlist(url):
    """Baixa uma playlist do SoundCloud."""
    subprocess.run(f'{SCDL_PATH} -l "{url}" -f --path "{os.path.abspath(DOWNLOAD_FOLDER)}"', shell=True)

def obter_info_musica(url):
    """Obtém título e imagem de capa."""
    try:
        html = requests.get(url).text
        title = re.search(r'<title>(.*?)\| SoundCloud</title>', html)
        image = re.search(r'<meta property="og:image" content="(.*?)">', html)
        return title.group(1).strip() if title else "Desconhecido", image.group(1).replace("-large", "-t500x500") if image else ""
    except:
        return "Desconhecido", ""

def adicionar_metadata(mp3_path, title, artist, album, cover_url):
    """Adiciona metadados ao MP3."""
    try:
        audio = MP3(mp3_path, ID3=ID3)
        if audio.tags is None:
            audio.tags = ID3()
        audio.tags.update({
            "TIT2": TIT2(encoding=3, text=title),
            "TPE1": TPE1(encoding=3, text=artist),
            "TALB": TALB(encoding=3, text=album)
        })
        if cover_url and cover_url.startswith("http"):
            audio.tags["APIC"] = APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=requests.get(cover_url).content)
            print(Fore.GREEN + "Capa adicionada!")
        audio.save()
        print(Fore.GREEN + f"Metadados adicionados a {mp3_path}")
    except Exception as e:
        print(Fore.RED + f"❌ Erro ao adicionar metadados: {e}")

def processar_download(url, tipo):
    """Gerencia o download e metadados."""
    limpar_terminal()
    exibir_banner()
    aviso_vpn()
    print(Fore.YELLOW + f"Baixando {tipo}...")
    baixar_playlist(url)
    title, cover_url = obter_info_musica(url)
    print(Fore.CYAN + f"🎵 Título: {title}\n📷 Capa: {cover_url}")
    for mp3_file in [f for f in os.listdir(DOWNLOAD_FOLDER) if f.endswith(".mp3")]:
        adicionar_metadata(os.path.join(DOWNLOAD_FOLDER, mp3_file), os.path.splitext(mp3_file)[0], "SoundCloud", "Playlist", cover_url)
    print(Fore.GREEN + "Download concluído!")
    bipar()

# Execução do menu
while True:
    escolha = input(Fore.MAGENTA + "\n1 - Baixar Música\n2 - Baixar Playlist\n3 - Atualizar\n99 - Sair\nOpção: ")
    if escolha in ["1", "2"]:
        processar_download(input(Fore.CYAN + "Digite a URL: "), "música" if escolha == "1" else "playlist")
    elif escolha == "3":
        print("\n Iniciando atualização...")
        os.system("bash ~/SoundJao/atualizar.sh")
        break  # Sai do loop após iniciar a atualização
    elif escolha == "99":
        print(Fore.RED + "Saindo...")
        break
    else:
        print(Fore.RED + "Opção inválida.")
