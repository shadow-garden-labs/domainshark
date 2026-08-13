#!/usr/bin/python3

"""This is the DomainShark module.

This module does domain scanning and intel recon.
"""

from fastapi import FastAPI
from pydantic import BaseModel


__all__ = [
    'DomainShark'
]

__version__ = '0.0.1'

__author__ = 'Cid Kagenou'


app = FastAPI(title="DomainShark", description="A simple FastAPI project guide")

default_subdomains = 'src/assets/subdomain_names.txt'


class DomainShark(BaseModel):

    target: str

    ports: list

    subdomains_file: str

    record_types: list


# Mock database matrix
fake_db = [
    {
        "id": 1,
        "target": "google.com",
        "ports":[80, 88],
        "subdomains_file": "/path/to/subdomain/file.txt",
        "record_types": ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT", "PTR", "SRV", "CAA", "DNAME"]
    },
    {
        "id": 2,
        "target": "reddit.com",
        "ports":[120, 62],
        "subdomains_file": "/different/path/to/subdomain/file.txt",
        "record_types": ["CNAME", "MX", "NS", "SOA"]
        },
]

@app.get("/")
def read_root():
    return {"message": "Welcome to Domain"}


@app.get("/target/{target_id}")
def get_target(target_id: int):
    return{
        "target_id": target_id
    }

@app.get("/target/", response_model=list[DomainShark])
def get_all_targets():

    return fake_db


@app.post("/target/")
def create_target(domain_target: DomainShark):

        return {
        "status": "target located",
        "Target Data": domain_target.target,
        "Port Data": domain_target.ports,
        "SubDomain File": domain_target.subdomains_file,
        "Record Data": domain_target.record_types
    }


@app.get("/target/{target_id}/forward-dns")
def get_forward_dns(self):

    pass


@app.get("/target/{target_id}/reverse-dns")
def get_reverse_dns(self):

    pass

@app.get("/target/{target_id}/subdomains")
def subdomain_scanner(self): # Print a message if no subdomains are found.

    pass

@app.get("/target/{target_id}/protscan")
def get_portscanner(self):
 
    pass


@app.get("/target/{target_id}/os-details")
def os_details(self):
    # Retrieve os details.
    pass


@app.get("/target/{target_id}/host-status")
def host_status(self):
    # Retrieve host status.
    pass


@app.get("/target/{target_id}/running-services")
def running_services(self, port):
    # Retrieve running services on port.
    pass


@app.get("/target/{target_id}/traceroute")
def traceroute(self):
    # Retrieve exact pathway to target.
    pass


@app.get("/target/{target_id}/whois")
def whois_ip_address(self):
    # Retrieve whois data.
    pass


@app.get("/target/{target_id}/ans-number")
def domain_asn_number(self):
    # Return Autonomous System Number (ANS), globally unique 16-bit or 32-bit number assigned to a network that manages a specific block of IP addresses.
    pass


@app.get("/target/{target_id}/dns-resolver")
def dns_resolver(self):

    pass


@app.get("/target/{target_id}/report")
def report(self):

    report = {} # Generate a human readable report of data retieved from the domain name.

    return report
