# 🎵 Baixar Playlists com Flask

Projeto em Flask para baixar músicas ou playlists com qualidade máxima e capas originais, via interface web simples e responsiva.

---

## 🚀 Funcionalidades

- Baixe músicas e playlists do SoundCloud ou similares.
- Interface bonita com Bootstrap e animações.
- Exibe status de download com `loading`.

---

## 📦 Requisitos

- Python 3.8+
- `yt-dlp` (ferramenta para baixar músicas)
- pip

---

## 🧪 Instalação

### 🔹 Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install yt-dlp
python app.py
```

### 🔹 Termux (Android)

```bash
pkg update && pkg upgrade
pkg install python git -y
pip install yt-dlp flask
git clone https://github.com/usuario/repositorio.git
cd repositorio
python app.py
```

### 🔹 Windows

1. Instale o [Python](https://www.python.org/downloads/)
2. Clone o repositório:
```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install yt-dlp
python app.py
```

### 🔹 MacOS

```bash
brew install python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install yt-dlp
python app.py
```

---

## 🌐 Rotas do Flask

- `/` → Página principal com input para URL e botão de download.
- `/baixar` → Rota AJAX que processa o download.
- `/sobre` → Página com informações do projeto.
- `/versao` → Página com a versão atual.

---

## 📄 Versão

Versão 1.3 (Beta)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 💡 To-Do Futuro

- [ ] Suporte para YouTube.
- [ ] Exibição de progresso do download.
- [ ] Histórico de downloads.