from cutter import db


class Link(db.Model):
    short_url = db.Column(db.String(40), primary_key=True)
    long_url = db.Column(db.String(2000), unique=True)

    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url

    def __repr__(self):
        return '<Link %r>' % self.short_url
