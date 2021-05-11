import requests
import datetime

prompt = "What would you like to know? You may enter: location, passover or people: "
err_prompt = "You may enter: 'location', 'passover', or 'people'"
api_base_url = "http://api.open-notify.org/"


def format_date(timestamp):
    """Format a UNIX timestamp object to datetime format"""
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def get_location_data():
    """Returns current location of ISS"""

    location_now_data = requests.get(api_base_url + "iss-now.json").json()

    if location_now_data["message"] == "success":
        unix_timestamp = location_now_data["timestamp"]
        formatted_timestamp = format_date(unix_timestamp)
        location = str(location_now_data["iss_position"])[1:-1]
        response = f"The ISS current location at this time: {formatted_timestamp} is {location}"

    else:
        response = "Error connecting to API"

    return response


def get_people_data():
    """Return People aboard ISS"""

    people_data = requests.get(api_base_url + "astros.json").json()

    if people_data["message"] == "success":
        names = [i['name'] for i in people_data['people']]
        formatted_names = ', '.join(str(x) for x in names)
        response = f"There are {len(names)} people aboard the ISS. Their names are: {formatted_names}"

    else:
        response = "Error connecting to API"

    return response


def get_passover_data():
    """Currently depreciated per ISS website - Not Active.
    Will allow input for test reasons
    """

    try:
        latitude = float(input("Enter a latitude as an integer: "))
        longitude = float(input("Enter a longitude as an integer: "))

        response = (f"ISS API has depreciated Passover Predictions. Therefore, we cannot confirm when the ISS will "
                    f"passover latitude: {latitude} and longitude: {longitude}")

    except ValueError:
        return f"This is not a valid input"

    return response


def process_request(req):
    """read in user input- raise error if unreadable"""

    user_input = req.lower()

    try:
        if user_input == 'location' or 'loc' in user_input:
            return get_location_data()
        elif user_input == 'people':
            return get_people_data()
        elif user_input == 'passover' or 'pass' in user_input:
            return get_passover_data()
        elif user_input == 'exit':
            exit()
        else:
            return f"This is not a valid input: {user_input}"
    except ValueError as err:
        return f"This is not a valid input: {user_input}. {err_prompt}"
