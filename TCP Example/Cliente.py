#!/usr/bin/env python3

import socket
import time

HOST = '192.168.43.169'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while(1):
        s.sendall(b'Hola alejo como esta?\n')
        time.sleep(1)
    s.close()
