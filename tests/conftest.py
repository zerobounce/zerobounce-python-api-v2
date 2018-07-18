import pytest
from zerobounce.helper import ZeroBounceAPI


@pytest.fixture
def zerobounce():
    return ZeroBounceAPI(123456)


@pytest.fixture
def zerobounce_response_validate():
    return {
         "address":"flowerjill@aol.com",
         "status":"valid",
         "sub_status":"",
         "free_email": True,
         "did_you_mean": None,
         "account":"flowerjill",
         "domain":"aol.com",
         "domain_age_days": "8426",
         "smtp_provider":"yahoo",
         "mx_record":"mx-aol.mail.gm0.yahoodns.net",
         "mx_found": True,
         "firstname":"Jill",
         "lastname":"Stein",
         "gender":"female",
         "country":"United States",
         "region":"Florida",
         "city":"West Palm Beach",
         "zipcode":"33401",
         "processed_at":"2017-04-01 02:48:02.592"
        }

@pytest.fixture
def zerobounce_response_getcredits():
    return {"Credits": 2375323}
