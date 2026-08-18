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

DEFAULT_SUBDOMAIN = 'src/assets/subdomain_names.txt'


class Sublist3r():

    def __init__(self, subdomain_textfile=DEFAULT_SUBDOMAIN):

        self.subdomains_file = open(subdomain_textfile, 'r')


    def __enter__(self):

        print('[+] OPENING FILE')

        self.subdomains = self.subdomains_file.read().splitlines()
    
        return self # Bound to the 'as' variable


    def __exit__(self, exc_type, exc_value, exc_traceback):

        self.subdomains_file.close()

        print('[+] CLOSING FILE')

        # Cleanup code goes here
        if exc_type:

            print(f'An error occured: {exc_value}')

        return False # Do not suppress exceptions


    def validate_url(url):

        pass


    def subdomain_scanner(self, domain_name): # Print a message if no subdomains are found.

        print(f"Debugging subdomains list: {self.subdomains}")
        subdomain_dict = {"Subdomain URLs": []}
        
        # loop for getting URL's
        for subdomain in self.subdomains:
        
            # making url by putting subdomain one by one
            url = f'https://{subdomain}.{domain_name}'
            
            # using try catch block to avoid crash of the
            # program
            try:
                # sending get request to the url
                requests.get(url)
                
                # if after putting subdomain one by one url 
                # is valid then printing the url
                subdomain_dict["Subdomain URLs"].append(url)
                
                # if url is invalid then pass it
            except (requests.ConnectionError, requests.Timeout):

                pass
        
        # Print a message if no subdomains were found
            if not subdomain_dict["Subdomain URLs"]:

                return f"[-] No subdomains found for IP address: {domain_name}"

            else:
                # print(f"[+] Found {len(subdomain_dict['Subdomain URLs'])} subdomain(s) for {domain_name}.")
                return subdomain_dict


    def find_prefixes(self):
        # use [+] in print statements/outputs
        
        print(f'[+] locating prefixes ...')


    def update_file(self):
        
        print(f'[+] updating file event ...')


    def remove_duplicates(self):
        
        print(f'[+] updating file event ...')
