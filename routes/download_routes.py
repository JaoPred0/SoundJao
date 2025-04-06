from flask import Blueprint, request, jsonify, send_file, current_app
import subprocess
import os

download_bp = Blueprint('download', __name__)

@download_bp.route('/baixar', methods=['POST'])
def baixar_musica():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"erro": "Forneça uma URL válida do SoundCloud"}), 400

    try:
        output_file = os.path.join(current_app.config['DOWNLOAD_FOLDER'], "%(title)s.%(ext)s")

        comando = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "-o", output_file,
            url
        ]

        subprocess.run(comando, check=True)

        arquivos = sorted(
            os.listdir(current_app.config['DOWNLOAD_FOLDER']),
            key=lambda x: os.path.getctime(os.path.join(current_app.config['DOWNLOAD_FOLDER'], x))
        )
        arquivo_baixado = arquivos[-1] if arquivos else None

        if not arquivo_baixado:
            return jsonify({"erro": "Nenhum arquivo foi baixado."}), 500

        caminho_completo = os.path.join(current_app.config['DOWNLOAD_FOLDER'], arquivo_baixado)
        return send_file(caminho_completo, as_attachment=True)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
