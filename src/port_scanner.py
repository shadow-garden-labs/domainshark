#!/usr/bin/python3

"""This is the PortScanner module.

This module does TCP Scanning Techniques, Stealth and Evasion Scans, and Other Probing Methods.
Port scans use network packets to find open, closed, or filtered communication ports on a target device.
"""

import json
import socket

__all__ = [
    'PortScanner'
]

__version__ = '0.0.1'

__author__ = 'Cid Kagenou'


class PortScanner():

    def __init__(self, ipaddress):

        self.ipaddress = ipaddress


    def tcp_port_scan(self, ports):
                
        open_ports = []
        
        ports_list = list(ports)

        for port in ports_list:

            # Create a TCP socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.settimeout(.25) # Fast timeout to skip closed ports
            
            # connect_ex returns 0 if the connection succeeded
            result = s.connect_ex((str(self.ipaddress), port))

            if result == 0:

                open_ports.append(port)

                print(f'[+] Port {port}: OPEN')
            
            else:

                print(f'[+] Port {port}: CLOSED')

            s.close()

        return open_ports


    def udp_port_scan(self):

        pass


    def syn_port_scan(self):

        pass


    def ack_port_scan(self):

        pass

    def xmas_port_scan(self):

        pass


    def stealth_port_scan(self):

        pass


    def null_port_scan(self):

        pass


    def example_port_scan_technique(self):

        pass