from core.clients.api_client import APIClient
import pytest
from datetime import datetime, timedelta
from faker import Faker

@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    client.auth()
    return client

@pytest.fixture
def booking_dates():
    today = datetime.today()
    checkin_date = today + timedelta(days=10)
    checkout_date = checkin_date + timedelta(days=5)
    return {
        "checkin": checkin_date.strftime('%Y-%m-%d'),
        "checkout": checkout_date.strftime('%Y-%m-%d')
    }

@pytest.fixture
def generate_random_booking_data(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": booking_dates,
        "additionalneeds": additionalneeds
    }
    return data

@pytest.fixture
def generate_custom_booking_data():
    data = {
        "firstname": "Balerino",
        "lastname": "Kapuchino",
        "totalprice": 228,
        "depositpaid": False,
        "bookingdates":{
            "checkin": "2025-05-26",
            "checkout": "2025-05-31"
        },
        "additionalneeds": "During news civil size ready answer know."
    }
    return data