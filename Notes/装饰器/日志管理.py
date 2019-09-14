import functools
import logging
import time

def logged(method):
    @functools.wraps(method)
    def inner(*args,**kw):
        start=time.time()
        return_value=method(*args,*kw)
        end=time.time()
        data=end-start
        logger=logging.getLogger('decorator.logged')
        logger.warn('Called method {0} at {1}; excution time{2}'
        'seconds; result {3}'.format(method.__name__,start,data,return_value))

    return inner

@logged
def lan():
    print('这是个普通的函数')
    
lan()