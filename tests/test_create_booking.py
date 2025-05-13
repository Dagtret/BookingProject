import allure
import pytest
import requests

@allure.feature('Test booking')
@allure.story('Test create booking')
def test_create_booking(api_client, generate_random_booking_data):
    status_code = api_client.create_booking(generate_random_booking_data)
    assert status_code == 201, f'Expected status 201 but got {status_code}'
