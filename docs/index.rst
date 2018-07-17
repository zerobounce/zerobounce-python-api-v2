.. ZeroBounce Python API documentation master file, created by
   sphinx-quickstart on Sat Dec  2 16:19:09 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ZeroBounce Python API's documentation!
=================================================

zerobounce-python-api
=====================

`ZeroBounce <https://www.zerobounce.net>`__ Python API.
The response object allows an attribute-like style access.


.. code:: python

    from zerobounce import ZeroBounceAPI

    zba = ZeroBounceAPI('yourapikey____________')
    print zba.get_credits()
    resp1 = zba.validate('flowerjill@aol.com')
    resp2 = zba.validatewithip('flowerjill@aol.com')

    print resp1
    {
      "address":"flowerjill@aol.com",
      "status":"Valid",
      "sub_status":"",
      "account":"flowerjill",
      "domain":"aol.com",
      "disposable":False,
      "toxic":False,
      "firstname":"Jill",
      "lastname":"Stein",
      "gender":"female",
      "location":None,
      "creationdate":None,
      "processedat":"2017-04-01 02:48:02.592"
    }

    print resp2
    {
      "address":"flowerjill@aol.com",
      "status":"Valid",
      "sub_status":"", 
      "account":"flowerjill",
      "domain":"aol.com",
      "disposable":False,
      "toxic":False,
      "firstname":"Jill",
      "lastname":"Stein",
      "gender":"female",
      "location":None,
      "country":"United States",
      "region":"Florida",
      "city":"West Palm Beach",
      "zipcode":"33401",
      "creationdate":None,
      "processedat":"2017-04-01 02:48:02.592"
    }

    print resp.firstname
    Jill

    print resp2.status
    Valid

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

