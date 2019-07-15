import sys
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        print('Empty Array')
        return None
    if len(ints) == 1:
        return (ints[0],ints[0])
    max = ints[0]
    min = ints[0]


    for i in range(1,len(ints)):
        val = ints[i]
        if val > max:
            max = val
        elif val < min:
            min = val
    return (min, max)
pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(get_min_max(l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [9]
print(get_min_max(l))
print ("Pass" if ((9, 9) == get_min_max(l)) else "Fail")

l = []
print ("Pass" if (None == get_min_max(l)) else "Fail")