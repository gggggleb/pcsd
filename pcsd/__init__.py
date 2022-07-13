# imports

import sys  # python sys module

from pcsd.db import Pcsd_db  # pcsd db class
from pcsd.net import main  # pcsd network class
from pcsd.test import test  # pcsd unit tests

# imports end

try:  # try running unit tests
    tests = sys.argv[1]  # get sys argv
    if tests == 'test':  # if sys argv = test
        test_db = Pcsd_db()  # create test db
        test(test_db)  # running unit test
except IndexError:  # sys argv not found
    pass  # passing run

try:  # try load config
    from config import *  # load conf

    # publish

    ip = ip
    port = port
    max_connect = max_connect
    config = 1  # config var edit

    # publish end
except ModuleNotFoundError:  # config not loaded
    config = 0  # config var edit

try:  # try load conf from argv
    ip = sys.argv[1]
    port = int(sys.argv[2])
    max_connect = int(sys.argv[3])
except IndexError:  # argv not funded
    if config == 0:  # load default config
        print('Argv not found use default')
        ip = '127.0.0.1'
        port = 4010
        max_connect = 10

db = Pcsd_db()  # create main db

print('PCSD is open source software publiched license GNU GPL3')

print('Binded', ip, port)

main(ip, port, max_connect, db)  # run network handler
