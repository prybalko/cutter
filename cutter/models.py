from cutter import db


class Link(db.Model):
    short_url_path = db.Column(db.String(32), primary_key=True)
    long_url = db.Column(db.String(2000), unique=True)

    def __init__(self, short_url_path, long_url):
        self.short_url_path = short_url_path
        self.long_url = long_url

    def __repr__(self):
        return '<Link %r>' % self.short_url_path
