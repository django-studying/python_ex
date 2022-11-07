import sys
import traceback

from exception_ex_396_1_2 import oops


def safe(func, *pargs, **kargs):
    try:
        func()
    except:
        print(sys.exc_info())
        traceback.print_exc(file=open('badly.exc', 'w'))


safe(oops)
