# imports

import glob  # python glob module
import os  # python os module
import pickle  # python pickle module


# end imports

class Pcsd_db:  # pcsd db class
    def __init__(self):  # class constructor
        self.db = {}  # create db
        for file in glob.glob("dump.pkl"):  # load db dump
            with open(file, 'rb') as f:  # open dump
                self.db = pickle.load(f)  # recreate db

    def set(self, key, value):  # set method
        try:
            self.db[key] = value  # write db
        except KeyError:  # key error
            return 'Key Error'  # return error

    def get(self, key):  # get method
        try:
            result = self.db[key]  # get from db
        except KeyError:
            return 'Key Error'
        return result  # return result

    def clear(self):  # clear methods
        self.db.clear()  # db clear

    def save(self):  # create dump
        with open('dump.pkl', 'wb') as f:
            pickle.dump(self.db, f)

    def rmdump(self):  # rm dump
        os.system('rm dump.pkl')  # rm dump
        self.clear()  # clear db

    def rm(self, key):  # rm key
        del self.db[key]  # write db

    def plus(self, key, value_plus):  # plus method
        try:
            value = self.db[key]  # get value
            result = value + value_plus  # plus
            self.db[key] = result  # write db
        except KeyError:
            return 'Key Error'

    def rename(self, key, keynew):  # rename method
        value = self.db.pop(key)  # delete and get value
        self.db[keynew] = value  # write db new key

    def find_key(self, key):  # find_key
        keys = self.db.keys()  # get keys on all db
        for db_key in keys:  # for
            if db_key == key:
                return 'Found'  # found
        return 'Not_found'  # not_found

    def find_value(self, value):  # find_value
        values = self.db.values()  # get keys on all db
        for db_value in values:  # for
            if db_value == value:
                return 'Found'  # found
        return 'Not_found'  # not_found
