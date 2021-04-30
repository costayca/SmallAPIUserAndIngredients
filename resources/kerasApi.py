from flask import Response, request
from flask_restful import Resource
from model.ingredientInit import model
from resources.imageHelper import load_img_from_bytes, predict_image

class KerasApi(Resource):
    def post(self):
        data = request.files
        image = data["img"]

        image = load_img_from_bytes(image)

        result = predict_image(model, image)

        return result