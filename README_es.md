[![Build Status](https://travis-ci.org/riquellopes/zerobounce-python-api.svg?branch=master)](https://travis-ci.org/riquellopes/zerobounce-python-api)
# zerobounce-python-api-v2

[ZeroBounce](https://www.zerobounce.net "Zerobounce Homepage") Python API v2.
The response object allows an attribute-like style access.


```python
from zerobounce import ZeroBounceAPI

zba = ZeroBounceAPI('yourapikey____________')
print zba.get_credits()
resp1 = zba.validate('flowerjill@aol.com','123.145.124.12')

print resp1
{
 "address":"flowerjill@aol.com",
 "status":"valid",
 "sub_status":"",
 "free_email":True,
 "did_you_mean":None,
 "account":"flowerjill",
 "domain":"aol.com",
 "domain_age_days": "8426",
 "smtp_provider":"yahoo",
 "mx_record":"mx-aol.mail.gm0.yahoodns.net",
 "mx_found": "True",
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

**Properties and possible values returned by:**
1. <b><i>validate</b></i> method
  
|<b>Property</b>|<b>Possible Values</b> 
|:--- |:--- 
address  | The email address you are validating. 
status | valid /invalid /catch-all /unknown /spamtrap /abuse /do_not_mail 
sub_status  |antispam_system /greylisted /mail_server_temporary_error /forcible_disconnect /mail_server_did_not_respond /timeout_exceeded /failed_smtp_connection /mailbox_quota_exceeded /exception_occurred /possible_trap /role_based /global_suppression /mailbox_not_found /no_dns_entries /failed_syntax_check /possible_typo /unroutable_ip_address /leading_period_removed /does_not_accept_mail /role_based_catch_all /disposable /toxic
account | The portion of the email address before the "@" symbol.
domain | The portion of the email address after the "@" symbol.
did_you_mean | Suggestive Fix for an email typo.
domain_age_days | Age of the email domain in days or [None].
free_email | [True/False] If the email comes from a free provider.
mx_found | [True/False] Does the domain have an MX record.
mx_record | The preferred MX record of the domain
smtp_provider | The SMTP Provider of the email or [None] (BETA).
firstname | The first name of the owner of the email when available or [None].
lastname  |The last name of the owner of the email when available or [None].
gender |The gender of the owner of the email when available or [None].
country |The country the email signed up when ip address is provided or [None].
region |The region the email signed up when ip address is provided or [None].
city |The city the email signed up when ip address is provided or [None].
zipcode |The zipcode the email signed up when ip address is provided or [None].
processed_at |The UTC time the email was validated.

2. <b><i>get_credits</b></i> method
  
|<b>Property</b>|<b>Possible Values</b> 
|:--- |:--- 
credits  | The number of credits left in account for email validation.

**Any of the following email addresses can be used for testing the API, no credits are charged for these test email addresses:**
+ disposable@example.com
+ invalid@example.com
+ valid@example.com
+ toxic@example.com
+ donotmail@example.com
+ spamtrap@example.com
+ abuse@example.com
+ unknown@example.com
+ catch_all@example.com
+ antispam_system@example.com
+ does_not_accept_mail@example.com
+ exception_occurred@example.com
+ failed_smtp_connection@example.com
+ failed_syntax_check@example.com
+ forcible_disconnect@example.com
+ global_suppression@example.com
+ greylisted@example.com
+ leading_period_removed@example.com
+ mail_server_did_not_respond@example.com
+ mail_server_temporary_error@example.com
+ mailbox_quota_exceeded@example.com
+ mailbox_not_found@example.com
+ no_dns_entries@example.com
+ possible_trap@example.com
+ possible_typo@example.com
+ role_based@example.com
+ timeout_exceeded@example.com
+ unroutable_ip_address@example.com
+ free_email@example.com

**You can this IP to test the GEO Location in the API.**

+ 99.110.204.1

```
