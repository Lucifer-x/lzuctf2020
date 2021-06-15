#!/usr/bin/python

import random,sys
import SocketServer
import os
import hashlib
from hashlib import sha256
import string
from secret import flag, N, e, d

assert e==65537
assert len(flag)==128
pt = int(flag.encode('hex'), 16)

class Task(SocketServer.BaseRequestHandler):
    def handle(self):
        self.request.sendall("LSB oracle\n")
        self.request.sendall("N: %d\n" % N)
        ct = pow(pt, e, N)
        self.request.sendall("The encrypted flag is: %d\n" % ct)
        while True:
            self.request.sendall("ciphertext: ")
            x = self.request.recv(2048)
            try:
                x = int(x)
            except:
                return
            m = pow(x, d, N)
            self.request.sendall("lsb is %d\n" % (m % 2))

        self.request.close()
            

class ThreadedServer(SocketServer.ForkingTCPServer, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 20001
    print(HOST)
    print(PORT)
    server = ThreadedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
