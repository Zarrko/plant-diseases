"""
Images Module
Contains REST API functions Image Requests from App/Website
"""
from app.api.images import webapp, logger
from app.api.images.schemas import PlantImagesSchema
from app.validators import validate_json
from flask import jsonify, request
from marshmallow.exceptions import ValidationError
from fastai.vision import *
import logging
import os

image_schema = PlantImagesSchema()
model_path = os.getcwd() + '/api/images/model'


@webapp.route("/")
@webapp.route("/images", methods=["POST"])
@validate_json
def plant_disease_images():
    """Endpoint to handle Images as received from client

    :return: Dictionary with prediction from model
    :rtype: dict
    """

    payload = request.get_json()

    if not payload:
        return jsonify(dict(message="No Data Provided")), 400

    try:
        # Validate Request Body
        data = image_schema.load(payload)
        logging.info(f"Pushing Image to Model for Prediction: {data}")

        try:
            img = open_image(data.path)
            learner = load_learner(model_path)
            predictions = learner.predict(img)
            return jsonify(dict(
                success=True,
                predictions=str(predictions)
            )), 200

        except Exception as e:
            return jsonify(dict(
                message=e
            )), 500

    except ValidationError as v:
        return jsonify(dict(errors=[v.messages])), 422
