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
from sublist3r import Sublist3r
from port_scanner import PortScanner


__all__ = [
    'DomainShark'
]

__version__ = '0.0.1'

__author__ = 'Cid Kagenou'



class DomainShark():

    """A Class Template for testing and templates.

        Args:
            target -> domain name/ipaddress: domain  or ip address.
    """


    def __init__(self, target):

        self.target = target

        self.data_conversion()

        self.port_scan = PortScanner(self.ipaddress)

        self.record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT", "PTR", "SRV", "CAA", "DNAME"]


    def __repr__(self):

        return f"DomainShark(target: '{self.target}', domain name: '{self.domain_name}', ipaddress: {self.ipaddress})"


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


    def subdomain_scanner(self, subdomain_list: Sublist3r): # Print a message if no subdomains are found.

        print('----URL after scanning subdomains----')
        
        # loop for getting URL's
        for subdomain in subdomain_list.subdomains:
        
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


    def human_readable_domain(self):

        pass


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


    def report(self):

        report = {} # Generate a human readable report of data retieved from the domain name.

        return report



with Sublist3r() as test_subdomain:

    test_target = DomainShark('142.251.218.78')

    # test_target.subdomain_scanner(test)

    ports = [88, 99, 65]

    test_target.port_scan.tcp_port_scan(ports)

    # print(test_target.ipaddress)
    
    # print(test_subdomain.subdomains)