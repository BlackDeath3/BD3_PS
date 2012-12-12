#!/usr/bin/env python

import os
import sys
import socket

open_ports = []
min_port = 20
max_port = 22

def print_header():
    print("==================== BD3PS ====================")

def print_footer():
    print("===============================================")

def print_open():
    print("Open Ports:")
    for x in open_ports:
        print("\t *", x)

def main():
    os.system("cls")
    print_header()
    if 1 < len(sys.argv):
        targetHost = sys.argv[1]
    else:
        targetHost = input("Enter host to scan:")
    targetIP = socket.gethostbyname(targetHost)
    #scan reserved ports
    for i in range(min_port, max_port):
        os.system("cls")
        print_header()
        print("Begin scan on host:", targetIP, "from", min_port, "to", max_port)
        print("Scanning port: ", i, "...", sep = "")
        print_open()
        print_footer()
        s = socket.socket()
        result = s.connect_ex((targetIP, i))
        if 0 == result:
            open_ports.append(i)
        s.close()
    os.system("cls")
    print_header()
    print("End scan on host:", targetIP, "from", min_port, "to", max_port)
    print_open()
    print_footer()

main()