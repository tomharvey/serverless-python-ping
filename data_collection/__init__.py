from requests import get


def get_google():
    r = get('https://google.com/')
    return r
