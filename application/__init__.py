from flask import Flask

# from ..config import Config
from .db import database


app = Flask(__name__)

app.config.from_object("config.Config")

database.init_app(app)

from . import models  # noqa: E402,F401

with app.app_context():
    database.create_all()

from . import routes  # noqa: E402,F401
