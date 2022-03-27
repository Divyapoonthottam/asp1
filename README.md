# Instructions
## Pre-requisites
Please install the following.
* Latest version of git
* Latest version of Python (> Python 3.7) and ensure that pip is available
* Install flask module using the command `pip install flask`
* Install dnspython module using the command `pip install dnspython`
* Install beautifulsoup4 module using the command `pip install beautifulsoup4`
* Install requests module using the command `pip install requests`

## How to run?
On your local machine, do the following.
* Clone this repository using the command `git clone https://github.com/Divyapoonthottam/asp1.git`
* Run python_server.py in a console window using the command `python3 python_server.py`. This will run a Python web server with 2 end points - `/check-txt-record` and `/find-meta-tag-with-name`
* Open another console window and run test_meta_tag.py using the command `python3 test_meta_tag.py`. Enter url, metatag-name and the response from the server endpoint `/find-meta-tag-with-name` will be printed as output.
* In the second console window, run test_dns_record.py using the command `python3 test_meta_tag.py`. Enter domain-name, dns-txt-record and the response from the server endpoint `/check-txt-record` will be printed as output.

## Implementation details

### python_server.py : Python Web Server
* Created a python server using flask micro web framework - `python_server.py`.
* One API is implemented as POST and another as GET just to demonstrate different methods in which we can expose this functionality.
* Implemented a GET endpoint `/find-meta-tag-with-name` in it. This end point accepts an url and meta-tag-name as query parameters. It will check whether the given meta tag is present in the URL's HTML and return its content if found. Otherwise it will return 400 or 404 responses as per the operation result.
  * This API utilizes the functionality implemented in `url_utility.py`
  * In `url_utility.py`, there are 2 helper functions. First one gets the HTML source of any URL. Second helper function uses Beautifulsoup library  to convert the HTML string in to parsable datastructure. With find_all function metatag names are collected and converted in to a dictionary.Dictionary elements are then compared with the given metatag-name.
* Implemented a POST endpoint `/check-txt-record` in it. This endpoint accepts a domain name and a dns-text-record value in JSON format. It will return the provided dns-text-record value if it is a valid DNS TXT record for the given domain. Otherwise it will return 400 or 404 responses as per the operation result.
  * This API utilizes the functionality implemented in `dns_utility.py`
  * Utilizing the `dns.resolver()` functionality available in dnsresolve library, this finds all TXT records for a domain name. Given txt-record is compared with the collected domain dns-text-records.

### Tests :Clients for interfacing with the web server
* Two test files are added for checking the response of endpoints
* This project is solely concentrating on the backend development of a python web server.