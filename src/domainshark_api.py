#!/usr/bin/python3

"""This is the DomainShark module.

This module does domain scanning and intel recon.
"""

from fastapi import FastAPI
from pydantic import BaseModel


__all__ = [
    'Domain'
]

__version__ = '0.0.1'

__author__ = 'Cid Kagenou'


app = FastAPI(title="Domainshark", description="A simple FastAPI project guide")

default_subdomains = 'src/assets/subdomain_names.txt'


class Domain(BaseModel):

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

@app.get("/target/", response_model=list[Domain])
def get_all_targets():

    return fake_db


@app.post("/target/")
def create_target(domain_target: Domain):

        return {
        "status": "target received",
        "Target Data": domain_target.target,
        "Port Data": domain_target.ports,
        "SubDomain File": domain_target.subdomains_file,
        "Record Data": domain_target.record_types
    }

