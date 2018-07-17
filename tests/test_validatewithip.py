import responses


@responses.activate
def test_should_get_status_valid_when_validatewithip_lowerjill(
        zerobounce, zerobounce_response_validatewithip):

    url = 'https://api.zerobounce.net/v1/validatewithip?apikey=123456&ipaddress=99.123.12.122&email=flowerjill@aol.com'
    responses.add(responses.GET,
                  url,
                  json=zerobounce_response_validatewithip,
                  status=200)

    zerobounce = zerobounce.validatewithip("flowerjill@aol.com")

    assert zerobounce['status'] == "Valid"
    assert zerobounce['firstname'] == "Jill"
    assert zerobounce['lastname'] == "Stein"
