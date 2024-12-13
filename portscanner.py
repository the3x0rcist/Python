#!/bin/env python3

#my simple portscanner project

import sys
import socket

#variables


if len(sys.argv) != 3:
    print("Usage: ./portscanner <ip> <port>")
    sys.exit(1)

ip = sys.argv[1]

for port in range(1, int(sys.argv[2])):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip,port))
    except:
        print("[OPEN] port: ", port)
    s.close()



