from flask import Blueprint, render_template

bp = Blueprint('default', __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('default/index.html')
