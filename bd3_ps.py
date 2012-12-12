#!/usr/bin/env python

import os
import sys
import socket

open_ports = []

def print_header():
    print("==================== BD3PS ====================")

def print_footer():
    print("===============================================")

def print_open():
    print("Open Ports:")
    for x in open_ports:
        print("\t *", x)

def main():
    min_port = 0
    max_port = 1023

    os.system("cls")
    print_header()
    if 3 < len(sys.argv):
        min_port = int(sys.argv[2])
        max_port = int(sys.argv[3])
    elif 2 < len(sys.argv):
        max_port = int(sys.argv[2])
    if 1 < len(sys.argv):
        targetHost = sys.argv[1]
    else:
        targetHost = input("Enter host to scan:")
    targetIP = socket.gethostbyname(targetHost)
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