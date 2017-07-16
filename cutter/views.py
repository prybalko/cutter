import json

from flask import redirect, render_template
from werkzeug.exceptions import abort

from cutter import app
from cutter.forms import UrlForm
from cutter.lib import get_object_or_404, shorten_url
from cutter.models import Link


@app.route("/")
def home():
    return render_template('index.html', form=UrlForm())


@app.route("/<short_url>")
def redirect_to_origin(short_url):
    link = get_object_or_404(Link, short_url)
    return redirect(link.long_url)


@app.route("/shorten/", methods=['POST'])
def shorten_url_api():
    form = UrlForm()
    if not form.validate_on_submit():
        abort(400)
    long_url = form.long_url.data
    short_url = shorten_url(long_url)
    return json.dumps({'short_url': short_url})
