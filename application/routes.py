import os

from flask import jsonify, request

from . import app
from .db import database
from .models import Image


@app.route("/home")
@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/images", methods=["GET", "POST"])
def getImageList():
    if request.method == "GET":
        images = Image.query.all()
        imageList = []
        for image in images:
            imageList.append(image.serialize())
        # print(imageList)
        return jsonify(imageList)
    else:
        if "file" not in request.files:
            return jsonify({"upload_status": False, "Fail_reason": "invalid File"})
        file = request.files["file"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)
        image = Image(name=file.filename)
        database.session.add(image)
        database.session.commit()
        return path