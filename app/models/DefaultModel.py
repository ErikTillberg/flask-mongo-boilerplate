from datetime import datetime

from mongoengine import StringField, DateTimeField

from app.database import db


class DefaultModel(db.Document):

    text = StringField(required=True)
    created = DateTimeField(default=datetime.utcnow)

    def as_dict(self):

        return {
            'id': str(self.id),
            'text': self.text,
            'created': self.created.strftime('"%Y-%m-%dT%H:%M:%S.%fZ"')
        }
