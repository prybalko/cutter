import hashlib
from urlparse import urlparse

from werkzeug.exceptions import abort

from cutter import db
from cutter.models import Link

MIN_URL_LENGTH = 5


def get_object_or_404(model, pk):
    obj = model.query.get(pk)
    if not obj:
        abort(404)
    return obj


def base_n(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def shorten_url(long_url):
    parsed_url = urlparse(long_url)
    if not parsed_url.scheme:
        long_url = parsed_url._replace(**{"scheme": "http"}).geturl().replace('///', '//')

    hex_hash = hashlib.sha1(long_url.encode('utf-8')).hexdigest()
    _hash = short_url = base_n(int(hex_hash, 16), 62)

    for url_length in xrange(MIN_URL_LENGTH, len(_hash)+1):
        short_url = _hash[:url_length]
        link = Link.query.get(short_url)
        if not link:
            new_link = Link(short_url=short_url, long_url=long_url)
            db.session.add(new_link)
            db.session.commit()
            break
        if link.long_url == long_url:
            break
    return short_url
