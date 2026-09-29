#!/usr/bin/python3

"""This is the Sublist3r module.

This module does domain scanning and intel recon.
"""

import json
import requests

__all__ = [
    'Sublist3r'
]

__version__ = '0.0.1'

__author__ = 'Cid Kagenou'

DEFAULT_TEXTFILE = 'domainshark/src/assets/subdomain_names.txt'


class Sublist3r():

    def __init__(self, domain_name, text_file=DEFAULT_TEXTFILE):

        self.text_file = open(text_file, 'r')

        self.domain_name = domain_name

        self.url_list = []


    def __enter__(self):

        print('[+] OPENING FILE')

        self.subdomain_list = self.text_file.read().splitlines()
    
        return self # Bound to the 'as' variable


    def __exit__(self, exc_type, exc_value, exc_traceback):

        self.text_file.close()

        print('[+] CLOSING FILE')

        # Cleanup code goes here
        if exc_type:

            print(f'An error occured: {exc_value}')

        return False # Do not suppress exceptions


    def validate_urls(self):

        for subdomain in self.subdomain_list:

            url = f'https://{subdomain}.{self.domain_name}'

            try:
                # sending get request to the url
                requests.get(url)
            
                # if after putting subdomain one by one url 
                # is valid then printing the url
                self.url_list.append(url)
            
                # if url is invalid then pass it
            except (requests.ConnectionError, requests.Timeout):

                pass



with Sublist3r("google.com") as test:

    test.validate_urls()

    print(test.url_list)