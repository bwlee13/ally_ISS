import utils


def get_iss_info_by_input(req):
    """
    GET current iss information: Location, Passing by given coordinates, or People aboard
    from command-line input
    """
    user_request = utils.process_request(req)
    print(user_request)


if __name__ == '__main__':
    while True:
        request = input(utils.prompt)
        get_iss_info_by_input(request)
