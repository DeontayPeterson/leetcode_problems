import random
from math import ceil



# def isBadVersion(version: int, answer: int) -> bool:
#     if version > answer:
#         return False
#     if version < answer:
#         return True

def isBadVersion(version:int) -> bool:
    if version >= 23:
        return True
    if version < 23:
        return False


def firstBadVersion(n: int) -> int:

    lower = 0
    upper = n

    while upper - lower > 1:

        if lower == 0:
            if isBadVersion(ceil(upper/2)):
                upper = ceil(upper/2)
            else:
                lower = ceil(upper/2)
        else:
            x = ceil((upper-lower)/2) + lower
            if isBadVersion(x):
                upper = x
            else:
                lower = x
    return upper
        

firstBadVersion(100)




