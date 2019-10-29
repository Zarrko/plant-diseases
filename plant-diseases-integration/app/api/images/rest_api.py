"""
Images Module
Contains REST API functions Image Requests from App/Website
"""
from app import logger
from app.api import images
from app.api.images.schemas import PlantImagesSchema
from app.validators import validate_json
from flask import jsonify, request
from marshmallow.exceptions import ValidationError
from fastai.vision import *

image_schema = PlantImagesSchema()
model_path = 'app/api/images/model'


@logger.catch
@images.route("", methods=["POST"])
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

        logger.info(f"Pushing Image to Model for Prediction: {data}")

        try:
            learner = load_learner(model_path)
            predictions = learner.predict(data)
            return jsonify(dict(
                success=True,
                predictions=predictions
            )), 200

        except Exception as e:
            logger.error(f"Failed to Predict Image with error {e}")
            return jsonify(dict(
                message="Failed to predict image"
            )), 500

    except ValidationError as v:
        logger.error(f"Failed to load schema with error {v}")
        return jsonify(dict(errors=[v.messages])), 422
