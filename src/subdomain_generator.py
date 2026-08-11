#!/usr/bin/python3

"""This is the SubdomainGenerator module.

This module does domain scanning and intel recon.
"""

import json

__all__ = [
    'SubdomainGenerator'
]

__version__ = '0.0.1'

__author__ = 'Cid Kagenou'

SUBDOMAIN_TEXTFILE = 'src/assets/subdomain_names.txt'


class SubdomainGenerator():

    def __init__(self, file_location):

        self.file_location = file_location


    def find_prefixes(self):
        # use [+] in print statements/outputs
        
        print(f'[+] locating prefixes ...')


    def update_file(self):
        
        print(f'[+] updating file event ...')


    def remove_duplicates(self):
        
        print(f'[+] updating file event ...')
