from collections import defaultdict
def sort_012_dic(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not input_list:
        return None
    val_dic = defaultdict()
    val_dic[0] = 0
    val_dic[1] = 0
    val_dic[2] = 0
    for val in input_list:
        val_dic[val] += 1

    for i in range(len(input_list)):
        while val_dic[0]>0:
            input_list[i] = 0
            val_dic[0] -= 1
            i += 1
        while val_dic[1]>0:
            input_list[i] = 1
            val_dic[1] -= 1
            i += 1
        while val_dic[2]>0:
            input_list[i] = 2
            val_dic[2] -= 1
            i += 1
    return input_list
    pass

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not input_list:
        return []
    val0 = 0
    val2 = len(input_list)-1

    output_list = [1]*len(input_list)

    for i in range(len(input_list)):
        if input_list[i] == 0 :
            output_list[val0] = 0
            val0 = val0+1
        elif input_list[i] == 2:
            output_list[val2] = 2
            val2 = val2 - 1

    return output_list
    pass

def sort_012_ideal(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not input_list:
        return []
    val0 = 0
    val2 = len(input_list)-1


    for i in range(len(input_list)):
        if input_list[i] == 0 :
            temp = input_list[val0]
            input_list[val0] = 0
            input_list[i] = temp
            val0 = val0+1
        elif input_list[i] == 2:
            temp = input_list[val2]
            input_list[val2] = 2
            input_list[i] = temp
            val2 = val2 - 1

    return input_list
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0])
test_function([])
test_function([2])