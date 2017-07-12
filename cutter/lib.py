from werkzeug.exceptions import abort
import hashlib

from cutter import db
from cutter.models import Link

MIN_URL_LENGTH = 6


def get_object_or_404(model, pk):
    obj = model.query.get(pk)
    if not obj:
        abort(404)
    return obj


def shorten_url(long_url):
    full_hash = short_url = hashlib.sha1(long_url).hexdigest()

    for url_length in xrange(MIN_URL_LENGTH, len(full_hash)+1):
        short_url = full_hash[:url_length]
        link = Link.query.get(short_url)
        if not link:
            new_link = Link(short_url=short_url, long_url=long_url)
            db.session.add(new_link)
            db.session.commit()
            break
        if link.long_url == long_url:
            break
    return short_url
