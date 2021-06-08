from flask import jsonify, request
from flask_restful import Resource
from model.fastaiModel import learn
from resources.imageHelper import load_img_fastai

class FastaiApi(Resource):
    def post(self):
        data = request.files
        image = data["img"]

        img = load_img_fastai(image)

        result = learn.predict(img)[0]
        return jsonify(result)