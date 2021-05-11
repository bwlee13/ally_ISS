import pytest
import testapp as app
import datetime


def format_date(timestamp):
    """Format a UNIX timestamp object to datetime format"""
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def get_location_data(data):
    """Returns current location of ISS"""

    location_now_data = data

    if location_now_data["message"] == "success":
        unix_timestamp = location_now_data["timestamp"]
        formatted_timestamp = format_date(unix_timestamp)
        location = str(location_now_data["iss_position"])[1:-1]
        response = f"The ISS current location at this time: {formatted_timestamp} is {location}"

    else:
        response = "Error connecting to API"

    return response


def process_request(req):
    """read in user input- raise error if unreadable"""

    user_input = req.lower()

    if user_input == 'location' or 'loc' in user_input:
        return 'location'
    elif user_input == 'people':
        return 'people'
    elif user_input == 'passover' or 'pass' in user_input:
        return 'passover'


def location_transformation():
    pass_test_input = {
        'timestamp': 1620749306,
        'iss_position': {
            'latitude': '-28.3193',
            'longitude': '-103.1801'
            },
        'message': 'success',
        }

    fail_test_input = {
        'timestamp': 1620749306,
        'iss_position': {
            'latitude': '-28.3193',
            'longitude': '-103.1801'
        },
        'message': 'fail',
    }

    pass_expected_output = "The ISS current location at this time: 2021-05-11 12:08:26 is 'latitude': '-28.3193', 'longitude': '-103.1801'"

    return pass_test_input, fail_test_input, pass_expected_output


def test_always_passes():
    assert True


def test_get_location():
    pass_test_input, fail_test_input, pass_expected_output = location_transformation()
    assert get_location_data(pass_test_input) == pass_expected_output


def test_fail_to_connect_to_api():
    pass_test_input, fail_test_input, pass_expected_output = location_transformation()
    assert get_location_data(fail_test_input) == "Error connecting to API"


def test_process_request():
    assert process_request("location") == 'location'
    assert process_request("people") == 'people'
    assert process_request("passover") == 'passover'

