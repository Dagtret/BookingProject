import allure

@allure.feature('Test booking')
@allure.story('Test create booking')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(booking_data=generate_random_booking_data)
    assert response["booking"]["firstname"] == generate_random_booking_data["firstname"], 'The firstname did not match the expected one'
    assert response["booking"]["lastname"] == generate_random_booking_data["lastname"], 'The lastname did not match the expected one'
    assert response["booking"]["totalprice"] == generate_random_booking_data["totalprice"], 'The totalprice did not match the expected one'
    assert response["booking"]["depositpaid"] == generate_random_booking_data["depositpaid"], 'The depositpaid did not match the expected one'
    assert response["booking"]["bookingdates"] == generate_random_booking_data["bookingdates"], 'The bookingdates did not match the expected one'
    assert response["booking"]["additionalneeds"] == generate_random_booking_data["additionalneeds"], 'The bookingdates did not match the expected one'