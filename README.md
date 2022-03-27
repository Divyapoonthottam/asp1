# Instructions
## Pre-requisites
Please install the following.
* Install git
* Latest version of Python (> Python 3.7) and ensure that pip is available
* Install flask module using the command `pip install flask`
* Install dnspython module using the command `pip install dnspython`
* Install beautifulsoup4 module using the command `pip install beautifulsoup4`
* Install requests module using the command `pip install requests`

## How to run?
On your local machine, do the following.
* Clone this repository `git clone https://github.com/Divyapoonthottam/asp1.git`
* Run python_server.py in a console window using `python3 python_server.py`. This will run a Python web server with 2 end points - `/check-txt-record` and `/find-meta-tag-with-name`
* Open another console window and run test_meta_tag.py using `python3 test_meta_tag.py`. Enter url, metatag-name and the response from the server endpoint `/find-meta-tag-with-name` will be printed as output.
* In the second console window, run test_dns_record.py using `python3 test_meta_tag.py`. Enter domain-name, dns-txt-record and the response from the server endpoint `/check-txt-record` will be printed as output.

## Implementation details
### python_server.py : Python Web Server
* Created a python server using flask micro web framework.
* Created an endpoint which receives an url and meta-tag-name, give response whether the meta-tag-name is present in its source code. Here json request is received with "get" method.
  * created endpoint which recieves a domain name and a dns-text-record.Giving response whether the dns-text-record is present in the given domain.rrequest is recieved by post method  
* url_utility
  * Using Beautifulsoup class convert a html file in to parsable datastructure.with find_all fuction metatag names are collected and converted in to a dictionary.dictionary elements are then compared with the given metatag-name.
* dns-utility
     * With dns.resolver() find various records of a domain name.from the resolved  rdatatypes, RdataType.TXT is seperated and collected.Given txt-record is compared with the given domain dns-text-records.
* test
    * two test files are added for checking the response of     endpoints
* notes
  * This project is solely  concentrating on the backened developement of a python server.