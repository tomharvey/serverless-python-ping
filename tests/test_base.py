from service import get_google


def test_get_google():
    r = get_google({}, {})
    assert r['status_code'] == 200
