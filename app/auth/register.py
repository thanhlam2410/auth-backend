from app.auth import authModule
from werkzeug import exceptions
from flask import request
from jsonschema import validate
from app.models import ClientAccount, Country, db
from werkzeug.security import generate_password_hash

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
    validate(input, schema=schema)

    existingUser = ClientAccount.query.filter_by(email=input["email"]).first()
    country = Country.query.filter_by(code=input["country"]).first()

    print(existingUser)
    if existingUser:
        return "email_is_used", 400

    passwordHash = generate_password_hash(input["password"])
    countryId = None

    if country is not None:
        countryId = country.id

    user = ClientAccount(email=input["email"], password_hash=passwordHash,
                         first_name=input["firstName"], last_name=input["lastName"], country_id=countryId)

    db.session.add(user)
    db.session.commit()

    return 'OK'
