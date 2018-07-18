from .mini_attr_dict import AttrDict
import requests


class ZeroBounceAPI(object):
    """ Main object used for creating a connection to the ZeroBounce API."""

    def __init__(self, api_key):
        """Initialize the object with the API Key.

        The API Key is located in your ZeroBounce account:
        https://www.zerobounce.net/members/apikey/

        Args:
            api_key (str): A 32 bytes length string"""

        self.api_key = api_key
        self.url = "https://api.zerobounce.net/v2"

    def get_credits(self):
        """Get the number of credits available in your ZeroBounce account"""

        return int(
            requests.get("%s/%s" % (self.url, "getcredits"), params={"api_key": self.api_key}).json()["Credits"])

    def validate(self, email, ip_address=""):
        """Get the validation result for one email address

        Get information about the email address, such as
        bounce status, First Name, Last Name

        Args:
            email (str): A syntactically valid email address
            ip_address (str): The IP Address which was used to register the email. Can be an empty string."""

        return AttrDict(
            requests.get("%s/%s" % (self.url, "validate"), params={"email": email, "api_key": self.api_key, "ip_address": ip_address}).json())
