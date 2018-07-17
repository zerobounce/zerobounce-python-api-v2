from .mini_attr_dict import AttrDict
import requests


class ZeroBounceAPI(object):
    """ Main object used for creating a connection to the ZeroBounce API."""

    def __init__(self, apikey):
        """Initialize the object with the API Key.

        The API Key is located in your ZeroBounce account:
        https://www.zerobounce.net/members/apikey/

        Args:
            apikey (str): A 32 bytes length string"""

        self.apikey = apikey
        self.url = "https://api.zerobounce.net/v1"

    def get_credits(self):
        """Get the number of credits available in your ZeroBounce account"""

        return int(
            requests.get("%s/%s" % (self.url, "getcredits"), params={"apikey": self.apikey}).json()["Credits"])

    def validate(self, email):
        """Get the validation result for one email address

        Get information about the email address, such as
        bounce status, First Name, Last Name

        Args:
            email (str): A syntactically valid email address"""

        return AttrDict(
            requests.get("%s/%s" % (self.url, "validate"), params={"email": email, "apikey": self.apikey}).json())

    def validatewithip(self, email, ipaddress="99.123.12.122"):
        """Get the validation result for one email address, using an IP.

        Get information about the email address, such as
        bounce status, First Name, Last Name, using an IP Address
        for live validations.

        Args:
            email (str): A syntactically valid email address
            ipaddress (str, optional): Specify an IP Address to use (advanced)."""

        return AttrDict(
            requests.get(
                "%s/%s" % (
                    self.url, "validatewithip"),
                params={"email": email, "apikey": self.apikey, "ipaddress": ipaddress}).json())
