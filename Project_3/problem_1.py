def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number<0:
        return None
    if number == 0 or number == 1:
        return number
    return (sqrtHelper(1,number,number))


def sqrtHelper(x,y,number,result=0):
    if x>=y:
        return result
    mid = int((x+y)//2)
    val = mid*mid
    if val == number:
        return mid
    if val > number:
        return sqrtHelper(x,mid-1,number,result)
    return sqrtHelper(mid+1,y,number,mid)

print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")
