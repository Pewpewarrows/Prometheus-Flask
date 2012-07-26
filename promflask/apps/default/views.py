from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('default', __name__, template_folder='templates')

@bp.route('/')
def index():
    return redirect(url_for('.foo'))
    # return render_template('default/index.html')

@bp.route('/foo/')
def foo():
    return render_template('default/index.html')

@bp.route('/bar/')
def bar():
    return render_template('default/index.html')
