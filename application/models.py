import os
from datetime import datetime
from .db import database
from . import app


class Image(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(20), nullable=False, unique=True)
    upload_date = database.Column(
        database.Date, nullable=False, default=datetime.utcnow()
    )
    full_path = database.Column(
        database.String(50),
        nullable=False,
        # default=path.join(path.abspath(__file__), "staic", "image", str(name)),
    )

    def __init__(self, filename, upload_date=datetime.now()):
        self.name = filename
        self.full_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        self.upload_date = upload_date

    def serialize(self):
        return {
            "id": self.id,
            "name": self.imageName,
            "upload_date": str(self.upload_date),
            "url": self.url,
        }

    def __repr__(self):
        return f"{self.id} : {self.name}"

    @property
    def imageName(self):
        return self.name.split(".")[0]

    @property
    def url(self):
        return "static/image/" + self.name
