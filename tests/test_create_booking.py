import allure
import pytest
import requests

@allure.feature('Test booking')
@allure.story('Test create booking')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(booking_data=generate_random_booking_data)

