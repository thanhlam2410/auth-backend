from unittest import TestCase
from app.models import db, Country, ClientAccount
import json
from .setup import setupTestEnvironment, destroyTestEnvironment
import pytest
import jwt


@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv("JWT_SECRET_KEY", "Abc@1234")


def seedData():
    country = Country(code="VN", name="Viet Nam")
    user = ClientAccount.createClientUser(
        email="lamttt@mailnesia.com",
        password="test password",
        firstName="lam",
        lastName="tran",
        countryId=1,
    )

    db.session.add(country)
    db.session.add(user)
    db.session.commit()


class LoginTest(TestCase):
    def setUp(self):
        self.flaskApp = setupTestEnvironment(self)
        seedData()
        self.client = self.flaskApp.test_client()

    def tearDown(self):
        destroyTestEnvironment(self)

    def postLogin(self, email, password):
        return self.client.post(
            "/auth/login",
            data=json.dumps(
                dict(
                    email=email,
                    password=password,
                )
            ),
            content_type="application/json",
        )

    def getProfile(self, token: str):
        return self.client.get(
            "/profile/me",
            headers={
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json",
            },
        )

    def test_login(self):
        login = self.postLogin("lamttt@mailnesia.com", "test password")
        self.assertEqual(login.status_code, 200)

        loginData = json.loads(login.data.decode("utf-8"))
        self.assertIsNot(loginData["accessToken"], None)

        token = jwt.decode(loginData["accessToken"], "Abc@1234", algorithms="HS256")
        self.assertEqual(str(token["userId"]), "1")

        profile = self.getProfile(token=loginData["accessToken"])
        self.assertEqual(profile.status_code, 200)
