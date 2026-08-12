#!/usr/bin/python3

"""This is the DomainShark module.

This module does domain scanning and intel recon.
"""
import ipaddress
import requests
import socket
import sys
import ipaddress
import whois
from urllib.parse import urlparse
import re
import validators
from dns import resolver, reversename
import dns.resolver
import json
from fastapi import FastAPI


__all__ = [
    'DomainShark'
]

__version__ = '0.0.1'

__author__ = 'Cid Kagenou'


DEFAULT_SUBDOMAIN = 'src/assets/subdomain_names.txt'

class DomainShark():

    """A Class Template for testing and templates.

        Args:
            target -> domain name/ipaddress: domain  or ip address.
    """


    def __init__(self, target, ports, subdomain_textfile=DEFAULT_SUBDOMAIN): # ports are and optional parameter.

        self.target = target

        self.ports = list(ports)

        self.subdomains_file = open(subdomain_textfile, 'r')

        self.data_conversion()

        self.record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT", "PTR", "SRV", "CAA", "DNAME"]


    def target_conversion(self, data: str):

        #if the data is a domain name --> set it to self.target, and use the domain name to find the ip address
        if isinstance(data, str): 

            self.new_ipaddress = ipaddress.ip_address(data)

        #if the data is an ipaddress --> set it to self.ipaddress, and use the ipaddress to find the domain name.
        elif isinstance(data, ipaddress):

            self.new_ipaddress = data # Already a ipaddress type

        else:

            raise TypeError("Target must be a string")


    def __repr__(self):

        return f"DomainShark(target: '{self.target}', ports: {self.ports}, domain name: '{self.domain_name}', ipaddress: {self.ipaddress})"


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


    def data_conversion(self):

        try:

            if self.is_strict_domain():

                self.domain_name = self.target
                
                self.forward_dns()

            elif self.is_ipaddress():

                self.ipaddress = self.target

                self.reverse_dns()

        except TypeError:

            return f"Type Error: Expected 'ipaddress' or 'domain name', got '{type(ipaddress).__name__}'"


    def is_strict_domain(self):
        # Reject if it's a valid IPv4 or IPv6 address
        if validators.ipv4(self.target) or validators.ipv6(self.target):
            
            return False
        
        # Otherwise, evaluate standard domain validation
        return validators.domain(self.target) is True


    def is_ipaddress(self):

        if ipaddress.ip_address(self.target):

            return True

        else:

            return False


    def forward_dns(self):

        try:
            # Extract the clean hostname (e.g., 'www.google.com') from the URL
            hostname = urlparse(self.target).hostname
            
            # Fallback if the URL didn't have a protocol prefix (like 'google.com')
            if not hostname:

                hostname = self.target

            # Resolve hostname to IP address
            resolve_hostname = socket.gethostbyname(hostname)
            
            self.ipaddress = ipaddress.ip_address(resolve_hostname)

        except socket.gaierror:

            return 'Error: Invalid URL or unable to resolve hostname.'


    def reverse_dns(self):
        """
            When a reverse DNS lookup is performed, instead of returning "google.com" or "youtube.com", it returns the specific server node.

        """
        try:
            # gethostbyaddr returns a tuple: (hostname, aliaslist, ipaddrlist)
            target_info = socket.gethostbyaddr(self.target)

            self.domain_name = target_info[0]
            
        except socket.herror:

            return "Unknown (No Reverse DNS record found)"


    def subdomain_scanner(self): # Print a message if no subdomains are found.

        print('----URL after scanning subdomains----')
        
        # loop for getting URL's
        for subdomain in self.subdomains:
        
            # making url by putting subdomain one by one
            url = f'https://{subdomain}.{self.target}'
            
            # using try catch block to avoid crash of the
            # program
            try:
                # sending get request to the url
                requests.get(url)
                
                # if after putting subdomain one by one url 
                # is valid then printing the url
                print(f'[+] {url}')
                
                # if url is invalid then pass it
            except requests.ConnectionError:

                pass


    def portscanner(self):
        
        print(f"----Scanning Ports: {self.ip_address} ---- '{self.target}'----")
        
        open_ports = []
        
        for port in self.ports:

            # Create a TCP socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.settimeout(.25) # Fast timeout to skip closed ports
            
            # connect_ex returns 0 if the connection succeeded
            result = s.connect_ex((self.ip_address, port))

            if result == 0:

                open_ports.append(port)

                print(f'[+] Port {port}: OPEN')
            
            else:

                print(f'[+] Port {port}: CLOSED')

            s.close()

        return open_ports


    def os_details(self):
        # Retrieve os details.
        pass


    def host_status(self):
        # Retrieve host status.
        pass


    def running_services(self, port):
        # Retrieve running services on port.
        pass


    def traceroute(self):
        # Retrieve exact pathway to target.
        pass


    def whois_ip_address(self):
        # Retrieve whois data.
        pass


    def domain_asn_number(self):
        # Return Autonomous System Number (ANS), globally unique 16-bit or 32-bit number assigned to a network that manages a specific block of IP addresses.
        pass


    def dns_resolver(self):

        # Create a DNS resolver
        resolver = dns.resolver.Resolver()

        for record_type in self.record_types:
            # Performs DNS lookup for the defined domain and record type
            try:

                answers = resolver.resolve(self.target, record_type)

            except dns.resolver.NoAnswer:

                continue

            # Prints the results
            print(f"[+]: {record_type} records for {self.target}:")

            for rdata in answers:

                print(f"► {rdata}")

    
    def org_email_addresses(self):
        # Return organization domain-based emails.

        pass


    def report(self):

        report = {} # Generate a human readable report of data retieved from the domain name.

        return report



with DomainShark('google.com', range(87, 89)) as test_target:

    print(f'[+]: {repr(test_target)}')

    test_target.dns_resolver()