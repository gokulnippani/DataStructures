def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        print("no elements in an array.")
        return
    if len(input_list) == 1:
        return [input_list[0],0]
    input_list.sort()
    n1 = 0
    n2=0
    pow = 0
    n=0
    while n < len(input_list):
        n1 = n1+(10**pow)*input_list[n]
        n=n+1
        if n<len(input_list):
            n2 = n2+(10**pow)*input_list[n]
            n=n+1
        pow = pow+1

    return [n1,n2]
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[1],[1]]
test_function(test_case)