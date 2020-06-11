from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)


@main.route('/')
def about():
    return render_template('about.html')
