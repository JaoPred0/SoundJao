import os
from config import CONFIG
from colorama import Fore, Style

def baixar_musica(url):
    """Baixa a música do SoundCloud usando scdl"""
    print(Fore.YELLOW + "Baixando música... Aguarde." + Style.RESET_ALL)
    
    quality_flag = "--high-quality" if CONFIG["quality"] == "high" else ""
    playlist_flag = "-c" if CONFIG["download_playlist"] else ""
    cover_flag = "--add-metadata" if CONFIG["save_cover"] else ""

    os.system(f"scdl -l {url} {quality_flag} {playlist_flag} {cover_flag} -o {CONFIG['download_dir']}")
    
    print(Fore.GREEN + f"Música baixada em '{CONFIG['download_dir']}'" + Style.RESET_ALL)
