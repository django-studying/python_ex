import sys

x = []

class MyError(Exception): pass


def oops():
    m = MyError()
    raise m

def oops2():
    try:
        oops()
    except (MyError, IndexError):
        print(sys.exc_info()[0:2])


# if __name__ == '__main__':
#     oops2()
