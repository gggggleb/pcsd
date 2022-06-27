import sys

from pcsd.db import Pcsd_db
from pcsd.net import main
from pcsd.test import test

try:
    tests = sys.argv[1]
    if tests == 'test':
        test_db = Pcsd_db()
        test(test_db)
except IndexError:
    pass

try:
    from config import *

    ip = ip
    port = port
    max_connect = max_connect
    config = 1
except ModuleNotFoundError:
    config = 0

try:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    max_connect = int(sys.argv[3])
except IndexError:
    if config == 0:
        print('Argv not found use default')
        ip = '127.0.0.1'
        port = 4010
        max_connect = 10

db = Pcsd_db()

print('PCSD is open source software publiched license GNU GPL3')

print('Binded', ip, port)

main(ip, port, max_connect, db)
