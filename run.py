import os
import requests
import subprocess
import time
import winsound  # Para Windows
import re
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB
from colorama import Fore, Style, init
import pyfiglet

# Inicializa colorama para cores no terminal
init(autoreset=True)

# Versão do script
VERSAO = "v1.0"

# Configurações
SCDL_PATH = "scdl"  # Certifique-se de que está instalado corretamente
# Pergunta ao usuário onde deseja salvar os arquivos
DOWNLOAD_FOLDER = input(Fore.CYAN + "Digite o nome da pasta onde deseja salvar as músicas: ").strip()

# Criar a pasta, se não existir
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def exibir_banner():
    """Exibe um banner estilizado com a versão do script"""
    banner = pyfiglet.figlet_format("SoundCloud DL")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + f"Versão: {VERSAO}\n")
    print(Fore.GREEN + "🔽 Baixe músicas e playlists do SoundCloud facilmente!\n")

def bipar():
    """Emite três bipes no sistema."""
    for _ in range(3):
        winsound.Beep(1000, 300)  # Frequência de 1000Hz por 300ms
        time.sleep(0.3)  # Pequena pausa entre os bipes

def baixar_playlist(url):
    """Baixa uma playlist do SoundCloud usando scdl"""
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    # Definir o caminho absoluto
    download_path = os.path.abspath(DOWNLOAD_FOLDER)

    # Comando corrigido
    comando = f'{SCDL_PATH} -l "{url}" -f --path "{download_path}"'
    subprocess.run(comando, shell=True)


def obter_info_musica(url):
    """Obtém título e imagem de capa a partir do link da música"""
    try:
        response = requests.get(url)
        html = response.text
        
        title_match = re.search(r'<title>(.*?)\| SoundCloud</title>', html)
        image_match = re.search(r'<meta property="og:image" content="(.*?)">', html)
        
        title = title_match.group(1).strip() if title_match else "Desconhecido"
        thumbnail_url = image_match.group(1).replace("-large", "-t500x500") if image_match else ""
        
        return title, thumbnail_url
    except Exception as e:
        print(Fore.RED + f"❌ Erro ao obter info da música: {e}")
        return "Desconhecido", ""

def baixar_capa(url, filename):
    """Baixa a imagem de capa"""
    if not url or not url.startswith("http"):
        return None
    
    response = requests.get(url)
    capa_path = os.path.join(DOWNLOAD_FOLDER, filename)
    with open(capa_path, "wb") as file:
        file.write(response.content)
    
    return capa_path

def adicionar_metadata(mp3_path, title, artist, album, cover_url):
    """Adiciona título, artista e capa ao arquivo MP3 direto da URL da imagem"""

    try:
        audio = MP3(mp3_path, ID3=ID3)
        if audio.tags is None:
            audio.tags = ID3()
    except Exception as e:
        print(Fore.RED + f"❌ Erro ao carregar MP3: {e}")
        return

    # Adicionar metadados
    audio.tags["TIT2"] = TIT2(encoding=3, text=title)
    audio.tags["TPE1"] = TPE1(encoding=3, text=artist)
    audio.tags["TALB"] = TALB(encoding=3, text=album)

    # Se houver URL de capa, baixar e adicionar diretamente
    if cover_url and cover_url.startswith("http"):
        try:
            response = requests.get(cover_url)
            response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
            audio.tags["APIC"] = APIC(
                encoding=3,
                mime="image/jpeg",
                type=3,
                desc="Cover",
                data=response.content  # Passa a imagem como bytes diretamente
            )
            print(Fore.GREEN + "✅ Capa adicionada diretamente ao MP3!")
        except Exception as e:
            print(Fore.RED + f"❌ Erro ao baixar a capa: {e}")

    # Salvar alterações no arquivo MP3
    audio.save()
    print(Fore.GREEN + f"✅ Metadados adicionados a {mp3_path}")

def processar_download(url, tipo):
    """Faz o download da música ou playlist"""
    print(Fore.YELLOW + f"🔽 Baixando {tipo}...")

    if tipo == "musica" or tipo == "playlist":
        baixar_playlist(url)
    
    title, cover_url = obter_info_musica(url)
    print(Fore.CYAN + f"🎵 Título: {title}")
    print(Fore.CYAN + f"📷 Capa: {cover_url}")
    
    mp3_files = [f for f in os.listdir(DOWNLOAD_FOLDER) if f.endswith(".mp3")]
    if mp3_files:
        for mp3_file in mp3_files:
            mp3_path = os.path.join(DOWNLOAD_FOLDER, mp3_file)
            adicionar_metadata(mp3_path, os.path.splitext(mp3_file)[0], "SoundCloud", "Playlist", cover_url)  # Passa a URL diretamente
    
    print(Fore.GREEN + "✅ Download concluído!")
    bipar()  # Emitindo três bipes

# Exibir banner ao iniciar
exibir_banner()

# Menu de opções
while True:
    print(Fore.MAGENTA + "\nEscolha uma opção:")
    print(Fore.YELLOW + "1️ - Baixar Música")
    print(Fore.YELLOW + "2️ - Baixar Playlist")
    print(Fore.RED + "9️9️ - Sair")
    
    escolha = input(Fore.CYAN + "Opção: ")

    if escolha == "1":
        url = input(Fore.CYAN + "Digite a URL da música: ")
        processar_download(url, "musica")
    elif escolha == "2":
        url = input(Fore.CYAN + "Digite a URL da playlist: ")
        processar_download(url, "playlist")
    elif escolha == "99":
        print(Fore.RED + "👋 Saindo...")
        break
    else:
        print(Fore.RED + "❌ Opção inválida. Tente novamente.")

