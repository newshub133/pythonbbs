from flask import Blueprint, render_template

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/register')
def register():
    return render_template("regist.html")


@bp.route('/question')
def question():
    return render_template("question.html")


@bp.route('/search')
def search():
    return "Hello World!"


@bp.route('/login')
def login():
    return "Hello World!"