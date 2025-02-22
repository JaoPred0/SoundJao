import tkinter as tk
from tkinter import messagebox, filedialog
import platform
import webbrowser
from downloader import download_music

def iniciar_gui():
    root = tk.Tk()
    root.title("SoundJao - Downloader")

    sistema = platform.system()
    if sistema == "Windows":
        root.state('zoomed')  
    elif sistema in ["Linux", "Darwin"]:
        root.attributes("-fullscreen", True)

    root.config(bg="#ECF0F1")

    cor_navbar = "#2C3E50"
    cor_fundo = "#ECF0F1"
    cor_botao = "#3498DB"
    cor_texto = "#34495E"

    navbar = tk.Frame(root, bg=cor_navbar, height=80)
    navbar.pack(fill=tk.X)

    nav_label = tk.Label(navbar, text="SoundJao", fg="white", bg=cor_navbar, font=("Arial", 24, "bold"))
    nav_label.pack(side=tk.LEFT, padx=20, pady=20)

    def escolher_diretorio():
        caminho = filedialog.askdirectory()
        if caminho:
            caminho_entry.delete(0, tk.END)
            caminho_entry.insert(0, caminho)

    def iniciar_download():
        url = url_entry.get()
        caminho = caminho_entry.get()
        if not url:
            messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        elif not caminho:
            messagebox.showerror("Erro", "Por favor, escolha um diretório para salvar a música.")
        else:
            download_music(url, caminho)  
            messagebox.showinfo("Sucesso", f"Iniciando o download da URL: {url} para {caminho}")
            url_entry.delete(0, tk.END)
            caminho_entry.delete(0, tk.END)

    def abrir_instagram():
        webbrowser.open("https://www.instagram.com/jaoo.predo/")

    def abrir_github():
        webbrowser.open("https://github.com/JaoPred0")

    home_label = tk.Label(root, text="Bem-vindo ao SoundJao!", font=("Arial", 30, "bold"), fg=cor_texto, bg=cor_fundo)
    descricao_label = tk.Label(root, text="Com o SoundJao, você pode baixar músicas e playlists do SoundCloud.",
                               font=("Arial", 14), fg=cor_texto, bg=cor_fundo, justify="center")
    vpn_info_label = tk.Label(root, text="🔴 Atenção! Para baixar do SoundCloud, use uma VPN dos EUA!",
                              font=("Arial", 12, "bold"), fg="red", bg=cor_fundo)

    btn_home = tk.Button(navbar, text="Home", bg=cor_navbar, fg="white", border=0, font=("Arial", 14, "bold"),
                         command=lambda: mostrar_tela("home"))
    btn_home.pack(side=tk.RIGHT, padx=10)

    btn_download = tk.Button(navbar, text="Baixar", bg=cor_navbar, fg="white", border=0, font=("Arial", 14, "bold"),
                             command=lambda: mostrar_tela("download"))
    btn_download.pack(side=tk.RIGHT, padx=10)

    btn_sobre = tk.Button(navbar, text="Sobre", bg=cor_navbar, fg="white", border=0, font=("Arial", 14, "bold"),
                          command=lambda: mostrar_tela("sobre"))
    btn_sobre.pack(side=tk.RIGHT, padx=10)

    titulo_download = tk.Label(root, text="Página de Download", font=("Arial", 24, "bold"), fg=cor_texto, bg=cor_fundo)
    url_label = tk.Label(root, text="Insira a URL do SoundCloud", font=("Arial", 12), fg=cor_texto, bg=cor_fundo)
    url_entry = tk.Entry(root, width=60, font=("Arial", 12))

    caminho_label = tk.Label(root, text="Escolha o diretório para salvar a música", font=("Arial", 12), fg=cor_texto, bg=cor_fundo)
    caminho_entry = tk.Entry(root, width=60, font=("Arial", 12))
    escolher_caminho_btn = tk.Button(root, text="Escolher Caminho", bg=cor_botao, fg="white", font=("Arial", 12), command=escolher_diretorio)
    download_btn = tk.Button(root, text="Iniciar Download", bg=cor_botao, fg="white", font=("Arial", 12), command=iniciar_download)

    sobre_label = tk.Label(root, text="Sobre o SoundJao (Versão 3.0)", font=("Arial", 24, "bold"), fg=cor_texto, bg=cor_fundo)
    sobre_text = tk.Label(root, text="SoundJao é uma ferramenta para baixar músicas do SoundCloud.\nCriado por JaoPred0.",
                          font=("Arial", 14), fg=cor_texto, bg=cor_fundo, justify="center")
    btn_instagram = tk.Button(root, text="Siga no Instagram", bg=cor_botao, fg="white", font=("Arial", 12), command=abrir_instagram)
    btn_github = tk.Button(root, text="GitHub", bg=cor_botao, fg="white", font=("Arial", 12), command=abrir_github)

    def limpar_tela():
        for widget in root.winfo_children():
            if widget not in [navbar]:
                widget.pack_forget()

    def mostrar_tela(tela):
        limpar_tela()
        if tela == "home":
            home_label.pack(pady=30)
            descricao_label.pack(pady=20)
            vpn_info_label.pack(pady=30)
        elif tela == "download":
            titulo_download.pack(pady=15)
            url_label.pack(pady=10)
            url_entry.pack(pady=5)
            caminho_label.pack(pady=10)
            caminho_entry.pack(pady=5)
            escolher_caminho_btn.pack(pady=5)
            download_btn.pack(pady=20)
        elif tela == "sobre":
            sobre_label.pack(pady=20)
            sobre_text.pack(pady=10)
            btn_instagram.pack(pady=10)
            btn_github.pack(pady=10)

    mostrar_tela("home")
    root.mainloop()

if __name__ == "__main__":
    iniciar_gui()
