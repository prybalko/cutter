from flask import redirect, render_template

from cutter import app
from cutter.lib import get_object_or_404
from cutter.models import Link


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<short_url>")
def redirect_to_origin(short_url):
    link = get_object_or_404(Link, short_url)
    return redirect(link.long_url)


@app.route("/shorten/", methods=['POST'])
def shorten_api():
    return "OK"
