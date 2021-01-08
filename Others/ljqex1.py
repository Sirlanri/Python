import datetime
from math import sqrt
import numpy
def one():
    """
    docstring
    """

    t=datetime.datetime.now()
    print("{}时{}分{}秒".format(t.hour,t.minute,t.second))
    

def two():
    """
    docstring
    """
    array=[[1,2],[3,4],[5,6]]
    print(array[1])


def three():
    """
    docstring
    """
    userstr=list(input().split())
    intlist=[]
    for single in userstr:
        intlist.append(int(single))
    varNum=numpy.var(intlist,ddof=1)
    print('{:.2f}'.format(varNum))

three()