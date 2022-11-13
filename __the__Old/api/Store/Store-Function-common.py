"""

store something commonly used

"""
import time

#TODO 哎哎哎没写完
def timeit(f):
    # used to measure time,post time it takes to execute
    #for debug and test
    #also used to show the time it takes to execute
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        print(time.time()-start)
        return ret

    return wrapper

@timeit()
def time_get():
    """
    get time
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # example: 2019-01-01 00:00:00

time_now = time_get()
print(time_now)