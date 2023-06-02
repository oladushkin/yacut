from datetime import datetime

from yacut import db
from settings import BASE_URL
from urllib.parse import urljoin


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def get_to_dict(self):
        return dict(
            url=self.original
        )

    def post_to_dict(self):
        return dict(
            url=self.original,
            short_link=urljoin(BASE_URL, self.short)
        )

    def from_dict(self, data):
        for field in ('original', 'short'):
            if field in data:
                setattr(self, field, data[field])
