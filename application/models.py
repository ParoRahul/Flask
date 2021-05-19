"""Database Schema Defination module."""

import os
from datetime import datetime

from . import app
from .db import database


class Image(database.Model):
    """Image Schema defination."""

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
        """Pass Filename as argument.

        Args:
            filename (String): File name
            upload_date ([type], optional): [description]. Defaults to datetime.now().
        """
        self.name = filename
        self.full_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        self.upload_date = upload_date

    def serialize(self):
        """Returns Image as object.

        Returns:
            [object]: Image Object
        """
        return {
            "id": self.id,
            "name": self.imageName,
            "upload_date": str(self.upload_date),
            "url": self.url,
        }

    def __repr__(self):
        """Repr method for Image .

        Returns:
            [String]: image id : Image name
        """
        return f"{self.id} : {self.name}"

    @property
    def imageName(self):
        """Returns image name with out extentions.

        Returns:
            [string]: name with out extentions
        """
        return self.name.split(".")[0]

    @property
    def url(self):
        """Return image url.

        Returns:
            [string]: Image URL
        """
        return "static/image/" + self.name
