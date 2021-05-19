"""Router Module."""

import os

from . import app
from .db import database
from .models import Image

from flask import Response, jsonify, request


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
        print("Post Request Hit")
        print(request.files)
        if "file" not in request.files:
            return jsonify({"upload_status": False, "Fail_reason": "invalid File"})
        file = request.files["file"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)
        image = Image(filename=file.filename)
        database.session.add(image)
        database.session.commit()
        return Response(status=200)
