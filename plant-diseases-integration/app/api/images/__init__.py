# flake8: noqa
from flask import Blueprint
from app.__meta__ import api

url = f"{api.get('version', 'v1')}/{api.get('base_route', 'plant-diseases')}"

deals = Blueprint(
    name="Deals",
    import_name=__name__,
    url_prefix=f"/api/{url}/images",
    static_folder="static",
    template_folder="templates",
)

from . import rest_api
