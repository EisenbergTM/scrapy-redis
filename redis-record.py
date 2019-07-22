import redis
#上次记录的id——4609355
if __name__=='__main__':
    #rds      = redis.Redis(host='10.30.180.221',port=16379,password='xdrt@^oasdfasf=<',db=0)
    #rds      = redis.Redis(host='118.190.243.148',port=16379,password='xdrt@^oasdfasf=<',db=0)
    pool = redis.ConnectionPool(host='118.190.243.148',port='16379',password='xdrt@^oasdfasf=<')
    rds = redis.Redis(connection_pool=pool)
    #rds.set('shanxun',5451187)
    #rds.set('leting',1554516615)
    #rds.set('last_hot_id',0)
   
    print('shanxun:',rds.get('shanxun'))
    print('leting:',rds.get('leting'))
    print('leting_token:',rds.get('leting_headers'))
    print('last_hot_id:',rds.get('last_hot_id'))
