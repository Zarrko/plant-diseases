from flask import Flask

webapp = Flask(__name__)

from app.api.images import rest_api
webapp.run(debug=True)
