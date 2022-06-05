import glob
import os
import sys
import pickle
import socket

try:
    ip = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    print('Argv not found use default')
    ip = '127.0.0.1'
    port = 4010

max_connect = 10

print('PCSD is open source software publiched license GNU GPL3')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(max_connect)

print('Binded', ip, port)

db = {}

for file in glob.glob("dump.pkl"):
    with open(file, 'rb') as f:
        db = pickle.load(f)

while True:
    conn, addr = sock.accept()
    print('Connnected', addr)
    req = conn.recv(2048)
    req = req.decode()
    print(req)
    if req == 'set':
        key = conn.recv(2048)
        value = conn.recv(2048)
        key = key.decode()
        value = value.decode()
        try:
            db[key] = value
        except KeyError:
            print('Key Error')
            conn.close()

    if req == 'get':
        key = conn.recv(2048)
        key = key.decode()
        try:
            result = db[key]
        except KeyError:
            print('Key Error')
            conn.send('Key Error'.encode())
            continue
        conn.send(result.encode())
    if req == 'exit':
        sock.close()
        exit()
    if req == 'clear':
        db.clear()
    if req == 'save':
        with open('dump.pkl', 'wb') as f:
            pickle.dump(db, f)
    if req == 'rmdump':
        os.system('rm dump.pkl')
        db.clear()
    if req == 'ping':
        conn.send('PONG!'.encode())
    if req == 'rm':
        key = conn.recv(2048)
        key = key.decode()
        del db[key]
    if req == 'plus':
        key = conn.recv(2048)
        key = key.decode()
        value_plus = conn.recv(2048)
        value_plus = value_plus.decode()
        try:
            value = db[key]
            result = value + value_plus
            db[key] = result
        except KeyError:
            print('Key Error')
            conn.send('Key Error'.encode())
    if req == 'rename':
        key = conn.recv(2048)
        keynew = conn.recv(2048)
        key = key.decode()
        keynew = keynew.decode()
        value = db.pop(key)
        db[keynew] = value
