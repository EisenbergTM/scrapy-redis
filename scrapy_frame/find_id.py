# -*- coding: utf-8 -*-

    
#r = redis.Redis(host = '192.168.1.32', port = 16379, db = 9, password = 'xdrt@^oasdfasf=<')    

import redis
from hashlib import md5
import logging
import logging.handlers

class SimpleHash(object):
    def __init__(self, cap, seed):
        self._cap = cap
        self._seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self._seed * ret + ord(value[i])
        return (self._cap - 1) & ret
                                                                     

class BloomFilter(object):
    def __init__(self, name, redis_url, seeds):
        """
        :redis_url: host|port|password|dbindex
        """

        self._logger = logging.getLogger()
        arr = redis_url.split('|')
        self._redis_host = arr[0]
        self._redis_port = arr[1]
        self._redis_password = arr[2]
        self._redis_dbindex = arr[3]
        self._redis_pool = None
        self._name = name
        self._bit_size = 1 << 32
        self._hashfunc = []
        for seed in seeds:
            self._hashfunc.append(SimpleHash(self._bit_size, seed))
     
    def isContains(self, str_input):
        if not str_input:
            return False
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        str_input_md5 = m5.hexdigest()
        ret = True
        #name = self.key + str(int(str_input_md5[0:2], 16) % self.blockNum)

        r = self.create_redis_connection()
        if r is not None:
            for f in self._hashfunc:
                loc = f.hash(str_input_md5)
                ret = ret & r.getbit(self._name, loc)
        return ret
                                         
    def insert(self, str_input):
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        str_input_md5 = m5.hexdigest()
        r = self.create_redis_connection()
        try:
            for f in self._hashfunc:
                loc = f.hash(str_input_md5)
                r.setbit(self._name, loc, 1)
            return True
        except Exception:            
            return False

    def create_redis_connection(self):
        r = None;
        for  i in range(5):
            try:
                if self._redis_pool is None:
                    self._redis_pool=redis.ConnectionPool(host=self._redis_host,password=self._redis_password,port=self._redis_port,db=self._redis_dbindex)
                r = redis.Redis(connection_pool=self._redis_pool)
                if r is not None:
                    return r
            except Exception:
                self._redis_pool = None
            time.sleep(1)    
        return None

