from app.auth import authModule
from werkzeug import exceptions
from flask import request
from jsonschema import validate
from app.models import ClientAccount, Country
from flask.json import jsonify

schema = {
    "type": "object",
    "properties": {
            "firstName": {"type": "string", "minLength": 2, "maxLength": 100},
            "lastName": {"type": "string", "minLength": 2, "maxLength": 100},
            "email": {"type": "string", "format": "email"},
            "password": {"type": "string", "minLength": 8, "maxLength": 32},
            "country": {"type": "string", "enum": ["VN", "SG"]}
    },
    "required": ["firstName", "lastName", "email", "password", "country"]
}


@authModule.route('/register', methods=['POST'])
def doRegister():
    input = request.get_json()
    validate(
        instance=input, schema=schema)

    isEmailExisted = checkExistingEmail(email=input["email"])
    print("isEmailExisted", isEmailExisted)
    if (isEmailExisted):
        return {"error": "email is used"}, 400

    countryId = getCountryId(code=input["country"])
    if (countryId is None):
        return {"error": "invalid country"}, 400

    user = ClientAccount.createClientUser(
        email=input["email"], password=input["password"], firstName=input["firstName"], lastName=input["lastName"], countryId=countryId)

    return jsonify(user.toDict())


def checkExistingEmail(email):
    user = ClientAccount.query.filter_by(email=email).first()
    if user is None:
        return False
    else:
        return True


def getCountryId(code):
    country = Country.getCountryFromCode(code=code)
    if country is None:
        return None
    else:
        return country.id
