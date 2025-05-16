import requests
import pytest
import allure
from pydantic import ValidationError

from conftest import generate_random_booking_data
from core.models.booking import BookingResponse

@allure.feature('Test booking')
@allure.story('Test create booking with random data')
def test_create_booking_with_random_data(api_client, generate_random_booking_data, booking_dates):
    response = api_client.create_booking(booking_data=generate_random_booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')
    assert response["booking"]["firstname"] == generate_random_booking_data["firstname"], 'The firstname did not match the expected one'
    assert response["booking"]["lastname"] == generate_random_booking_data["lastname"], 'The lastname did not match the expected one'
    assert response["booking"]["totalprice"] == generate_random_booking_data["totalprice"], 'The totalprice did not match the expected one'
    assert response["booking"]["depositpaid"] == generate_random_booking_data["depositpaid"], 'The depositpaid did not match the expected one'
    assert response["booking"]["bookingdates"]["checkin"] == booking_dates["checkin"], 'The checkin date did not match the expected one'
    assert response["booking"]["bookingdates"]["checkout"] == booking_dates["checkout"], 'The checkout date did not match the expected one'
    assert response["booking"]["additionalneeds"] == generate_random_booking_data["additionalneeds"], 'The additionalneeds did not match the expected one'

@allure.feature('Test booking')
@allure.story('Test create booking with custom data')
def test_create_booking_with_custom_data(api_client, generate_custom_booking_data, generate_random_booking_data):
    response = api_client.create_booking(booking_data=generate_custom_booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise  ValidationError(f'Response validation failed: {e}')
    assert response["booking"]["firstname"] == generate_custom_booking_data["firstname"], 'The firstname did not match the expected one'
    assert response["booking"]["lastname"] == generate_custom_booking_data["lastname"], 'The lastname did not match the expected one'
    assert response["booking"]["totalprice"] == generate_custom_booking_data["totalprice"], 'The totalprice did not match the expected one'
    assert response["booking"]["depositpaid"] == generate_custom_booking_data["depositpaid"], 'The depositpaid did not match the expected one'
    assert response["booking"]["bookingdates"]["checkin"] == generate_custom_booking_data["bookingdates"]["checkin"], 'The checkin date did not match the expected one'
    assert response["booking"]["bookingdates"]["checkout"] == generate_custom_booking_data["bookingdates"]["checkout"], 'The checkout date did not match the expected one'
    assert response["booking"]["additionalneeds"] == generate_custom_booking_data["additionalneeds"], 'The additionalneeds did not match the expected one'

@allure.feature('Test booking')
@allure.story('Test create booking without firstname')
def test_create_booking_without_firstname(api_client, generate_random_booking_data):
    generate_random_booking_data['firstname'] = None
    with pytest.raises(requests.HTTPError) as exc_info:
        api_client.create_booking(booking_data=generate_random_booking_data)
    assert exc_info.value.response.status_code == 500, f'Expected status 500 but got {exc_info.value.response.status_code}'

@allure.feature('Test booking')
@allure.story('Test create booking with wrong data format in firstname')
def test_create_booking_with_wrong_data_format_in_firstname(api_client, generate_random_booking_data):
    generate_random_booking_data['firstname'] = 99
    with pytest.raises(requests.HTTPError) as exc_info:
        api_client.create_booking(booking_data=generate_random_booking_data)
    assert exc_info.value.response.status_code == 500, f'Expected status 500 but got {exc_info.value.response.status_code}'

#Дальше не буду расписывать, точно так же проверял бы и другие поля. Еще бы воспользовался техниками тест дизайна, дополнил бы, например, анализом граничных значений и т.д.