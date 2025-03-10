from flask import Flask, render_template, request, jsonify, send_file
import subprocess
import os

app = Flask(__name__)

# Pasta para salvar músicas baixadas
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/baixar', methods=['POST'])
def baixar_musica():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"erro": "Forneça uma URL válida do SoundCloud"}), 400

    try:
        output_file = os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s")

        comando = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "-o", output_file,
            url
        ]

        subprocess.run(comando, check=True)

        # Pegar o último arquivo baixado
        arquivos = sorted(os.listdir(DOWNLOAD_FOLDER), key=lambda x: os.path.getctime(os.path.join(DOWNLOAD_FOLDER, x)))
        arquivo_baixado = arquivos[-1] if arquivos else None

        if not arquivo_baixado:
            return jsonify({"erro": "Nenhum arquivo foi baixado."}), 500

        caminho_completo = os.path.join(DOWNLOAD_FOLDER, arquivo_baixado)
        return send_file(caminho_completo, as_attachment=True)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/versao')
def versao():
    return render_template("versao.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")
if __name__ == '__main__':
    app.run(debug=True)
