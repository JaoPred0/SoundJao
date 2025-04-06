from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template("index.html")

@main_bp.route('/versao')
def versao():
    return render_template("versao.html")

@main_bp.route('/sobre')
def sobre():
    return render_template("sobre.html")
