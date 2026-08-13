#!/usr/bin/python3

"""This is the Sublist3r module.

This module does domain scanning and intel recon.
"""

import json

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


    def find_prefixes(self):
        # use [+] in print statements/outputs
        
        print(f'[+] locating prefixes ...')


    def update_file(self):
        
        print(f'[+] updating file event ...')


    def remove_duplicates(self):
        
        print(f'[+] updating file event ...')
