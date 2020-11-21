from app.auth import authModule
from werkzeug import exceptions
from flask import request
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
            "firstName": {"type": "string", "minLength": 2, "maxLength": 100},
            "lastName": {"type": "string", "minLength": 2, "maxLength": 100},
            "email": {"type": "string", "format": "email"},
            "password": {"type": "string", "minLength": 8, "maxLength": 32}
    },
    "required": ["firstName", "lastName", "email", "password"]
}


@authModule.route('/register', methods=['POST'])
def doRegister():
    print(request.get_json())
    validate(
        instance=request.get_json(), schema=schema)
    return 'OK'
