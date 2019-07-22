import requests
import json
import time
import os

class Query_realtime():
    def __init__(self,app_id):
        self.app_id = app_id
        self.url = 'http://114.215.18.7:8010/HttpService2/grab_stat'
        


    def query_message(self):
        param = 'app_id='+str(self.app_id)+'&timestamp=1532597459&sign=xx'
        r=requests.get(self.url,params=param)
        js = json.loads(r.content)
        print(js['data'])
        return js['data']



if __name__=='__main__':
    qa = Query_realtime('dongjiu')
    qa.query_message()
    os._exit(0)
