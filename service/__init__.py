from requests import get


def get_google(event, context):
    r = get('https://google.com/')

    return {
        "status_code": r.status_code,
    }
