import subprocess
import os
import requests
import re
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC

SCDL_PATH = "scdl"

def baixar_playlist(url, caminho):
    """Baixa uma playlist do SoundCloud."""
    subprocess.run(f'{SCDL_PATH} -l "{url}" -f --path "{os.path.abspath(caminho)}"', shell=True)

def obter_info_musica(url):
    """Obtém título e imagem de capa."""
    try:
        html = requests.get(url).text
        title = re.search(r'<title>(.*?)\| SoundCloud</title>', html)
        image = re.search(r'<meta property="og:image" content="(.*?)">', html)
        return title.group(1).strip() if title else "Desconhecido", image.group(1).replace("-large", "-t500x500") if image else ""
    except Exception as e:
        print(f"❌ Erro ao obter informações: {e}")
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
            print("✅ Capa adicionada!")
        audio.save()
        print(f"✅ Metadados adicionados a {mp3_path}")
    except Exception as e:
        print(f"❌ Erro ao adicionar metadados: {e}")

def download_music(url, caminho):
    """Função principal para gerenciar o download e adicionar metadados."""
    print(f"🔽 Baixando a música ou playlist de {url}...")
    baixar_playlist(url, caminho)  # Baixa a playlist ou música

    title, cover_url = obter_info_musica(url)
    print(f"🎵 Título: {title}\n📷 Capa: {cover_url}")

    for mp3_file in [f for f in os.listdir(caminho) if f.endswith(".mp3")]:
        mp3_path = os.path.join(caminho, mp3_file)
        adicionar_metadata(mp3_path, title, "SoundCloud", "Playlist", cover_url)
    
    print("✅ Download e metadados concluídos!")
