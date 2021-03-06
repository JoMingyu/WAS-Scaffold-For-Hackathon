from functools import wraps

from flask import abort, request
from jsonschema import ValidationError, validate


def validate_with_jsonschema(jsonschema: dict):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if request.is_json:
                try:
                    validate(request.json, jsonschema)
                except ValidationError:
                    abort(400)

            return fn(*args, **kwargs)
        return wrapper
    return decorator
