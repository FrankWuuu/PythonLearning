# 修饰器
import functools
def totalfunc(text):
    def addfunc(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return addfunc


@totalfunc('try')
def now():
    print('time:20210402')


now()
print(now.__name__)
