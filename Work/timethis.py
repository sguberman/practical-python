# timethis.py

import time


def timethis(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = fn(*args, **kwargs)
        end = time.time()
        print('{}.{}: {:f}'.format(fn.__module__, fn.__name__, end - start))
        return r
    return wrapper
