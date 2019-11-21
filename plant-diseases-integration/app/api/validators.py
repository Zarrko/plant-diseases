from functools import wraps
from flask import (
    jsonify,
    request,
)


def validate_json(f):
    """
    Decorator function that validates a JSON request as received from a client.
    If the JSON is invalid a 400 response code with an error message is returned to the client
    :param f Function
    :returns tuple with JSONified dictionary response and 400 response status
    """
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.get_json()
        except Exception as e:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper