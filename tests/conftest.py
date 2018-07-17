import pytest
from zerobounce.helper import ZeroBounceAPI


@pytest.fixture
def zerobounce():
    return ZeroBounceAPI(123456)


@pytest.fixture
def zerobounce_response_validate():
    return {
        "address": "flowerjill@aol.com",
        "status": "Valid",
        "sub_status": "",
        "account": "flowerjill",
        "domain": "aol.com",
        "disposable": False,
        "toxic": False,
        "firstname": "Jill",
        "lastname": "Stein",
        "gender": "female",
        "location": None,
        "creationdate": None,
        "processedat": "2017-04-01 02:48:02.592"
    }


@pytest.fixture
def zerobounce_response_validatewithip():
    return {
        "address": "flowerjill@aol.com",
        "status": "Valid",
        "sub_status": "",
        "account": "flowerjill",
        "domain": "aol.com",
        "disposable": False,
        "toxic": False,
        "firstname": "Jill",
        "lastname": "Stein",
        "gender": "female",
        "location": None,
        "country": "United States",
        "region": "Florida",
        "city": "West Palm Beach",
        "zipcode": "33401",
        "creationdate": None,
        "processedat": "2017-04-01 02:48:02.592"
    }


@pytest.fixture
def zerobounce_response_getcredits():
    return {"Credits": 2375323}
