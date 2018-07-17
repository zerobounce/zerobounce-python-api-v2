[![Build Status](https://travis-ci.org/riquellopes/zerobounce-python-api.svg?branch=master)](https://travis-ci.org/riquellopes/zerobounce-python-api)
# zerobounce-python-api-v2

[ZeroBounce](https://www.zerobounce.net "Zerobounce Homepage") Python API v2.
The response object allows an attribute-like style access.


```python
from zerobounce import ZeroBounceAPI

zba = ZeroBounceAPI('yourapikey____________')
print zba.get_credits()
resp1 = zba.validate('flowerjill@aol.com')

print resp1
{
 "address":"flowerjill@aol.com",
 "status":"valid",
 "sub_status":"",
 "free_email":true,
 "did_you_mean":null,
 "account":"flowerjill",
 "domain":"aol.com",
 "domain_age_days": "8426",
 "smtp_provider":"yahoo",
 "mx_record":"mx-aol.mail.gm0.yahoodns.net",
 "mx_found": true,
 "firstname":"Jill",
 "lastname":"Stein",
 "gender":"female",
 "country":"United States",
 "region":"Florida",
 "city":"West Palm Beach",
 "zipcode":"33401",
 "processed_at":"2017-04-01 02:48:02.592"
}

print resp.firstname
Jill

print resp2.status
valid


```
