# imports

import socket
import threading
from _thread import *

from pcsd.handler import Net


# end imports

def main(ip, port, max_connect, db):
    conn_block = threading.Lock()  # create lock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
    sock.bind((ip, port))  # bind socket
    sock.listen(max_connect)  # max connections bind
    while True:  # Endless
        conn, addr = sock.accept()  # accept connection
        print('Connected!', addr)  # print connection
        conn_block.acquire()  # lock unlock
        status = conn.recv(2048)  # get status
        status = status.decode()  # decode status
        start_new_thread(Net, (db, sock, conn, status, conn_block))  # run handler
