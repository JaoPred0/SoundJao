from flask import Flask
from routes.main_routes import main_bp
from routes.download_routes import download_bp
import os

app = Flask(__name__)

# Pasta para salvar músicas baixadas
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Registrar rotas
app.register_blueprint(main_bp)
app.register_blueprint(download_bp)

if __name__ == '__main__':
    app.run(debug=True)
