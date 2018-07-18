import responses


@responses.activate
def test_should_get_status_valid_when_validate_lowerjill(
        zerobounce, zerobounce_response_validate):
    responses.add(responses.GET,
                  'https://api.zerobounce.net/v2/validate?api_key=123456&email=flowerjill@aol.com@ip_address=99.123.12.122',
                  json=zerobounce_response_validate,
                  status=200)

    zerobounce = zerobounce.validate("flowerjill@aol.com")

    assert zerobounce['status'] == "valid"
    assert zerobounce['firstname'] == "Jill"
    assert zerobounce['lastname'] == "Stein"
