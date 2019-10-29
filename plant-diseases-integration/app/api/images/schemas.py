"""
Schemas Module
This contains validation for Schema when handling images for model prediction
"""

from marshmallow import Schema, fields
from marshmallow.validate import Length


class PlantImagesSchema(Schema):
    """Image Details sent from Client
    Image Schema used to validate the request sent by client with Image data
    Attributes:
        path (str): Path to Image
    """
    path = fields.String(required=True, validate=Length(min=1))
