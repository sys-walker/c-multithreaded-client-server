#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,socket,signal
def sig_handler(signum, frame):
    if socket_fd !=None:
        socket_fd.close()
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sig_handler)

    server_name = ""

    server_port=0
    global socket_fd
    # socket_fd=None

    server_host=None

    server_adress=None

    # Get server name from command line arguments or stdin.
    if len(sys.argv)>1:
        server_name = sys.argv[1]
    else:
        server_name = input("Enter Server Name: ")

    #  Get server port from command line arguments or stdin.
    server_port = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    if not server_port:
        server_port= int(input("Enter Port: "))
    server_host = socket.gethostbyname(server_name)

    # Initialise IPv4 server address with server host.
    server_adress=(server_host, server_port)
    # Create TCP socket.
    socket_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to socket with server address
    socket_fd.connect(server_adress)

    """
    TODO: Put server interaction code here. For example, use
    socket_fd.send(prams)  and socket_fd.recv(TCP) /socket_fd.recv(UDP you know who has send it) to send and receive messages
    with the client.
    """

    socket_fd.close()
    pass
