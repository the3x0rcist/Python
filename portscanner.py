#!/bin/env python3

#my simple portscanner project

import sys
import socket

if len(sys.argv) != 3:
    print("Usage: ./portscanner <ip> <max_port>")
    sys.exit(1)

ip = sys.argv[1]
max_port = int(sys.argv[2])

for port in range(1, max_port + 1):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Set timeout for faster scanning
        # Attempt to connect to the target port
        s.connect((ip, port))
        print(f"[OPEN] Port: {port}")
    except:
        # Connection failed, port is closed or filtered
        pass
    finally:
        s.close()



