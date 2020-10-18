import numpy as np
from pandas import *

def read_file(name):
    """
    Reads a given file and returns a list where the first value is the number of test cases, and the second
    is a list of dictionaries, each of which contains the information to run a specific test case
    :param name: name of the file
    :return: List of information for test cases for shopping()
    """
    with open(name, 'r') as datafile:
        lines = datafile.read().splitlines()
    test_cases = []

    test_cases.append(lines[0])
    test_cases.append([])
    i = 1
    while i < len(lines):
        case_info = {
            "items": {0: 0},
            "capacities": []
            }
        # get # of items and iterate through and store info for this case
        items = int(lines[i])

        i+=1

        for n in range(items):
            item_desc = lines[i].split()    # item_desc[0] is price, #item_info[1] is weight
            items = case_info["items"]
            items[int(item_desc[0])] = int(item_desc[1])
            # do stuff with item
            i += 1

        # get # of members and iterate through and store info for this case
        members = int(lines[i])
        i += 1
        for m in range(members):
            case_info["capacities"].append(lines[i])
            # do stuff with member
            i += 1

        test_cases[1].append(case_info)

    return test_cases

def write_file(name):
    pass

def get_max_capacity(weight_list):
    max_capacity = 0
    for capacity in weight_list:
        max_capacity = max(max_capacity, int(capacity))
    return max_capacity

def main():
    test_case = read_file("shopping.txt")
    case_list = test_case[1]
    testcase_num = 0
    for case in case_list:
        testcase_num += 1
        items = case["items"]
        family = case["capacities"]
        num_items = len(items)
        maxCap = get_max_capacity(family)       # highest carrying capacity in family

        # create dynamic programming table to store all sub-problem results
        dpt = [[0 for x in range(maxCap+1)] for _ in range(num_items+1)]
        row = 1
        for item in items:
            if item == 0:
                pass
            else:
                item_weight = items[item]
                for capacity in range(1, maxCap+1):
                    if item_weight <= capacity:
                        dpt[row][capacity] = max(item + dpt[row - 1][capacity - item_weight],
                                                  dpt[row - 1][capacity])
                    else:
                        dpt[row][capacity] = dpt[row-1][capacity]
            row += 1

        print(testcase_num)
        print(DataFrame(dpt))
        """ 
        for item in range(1, num_items):
            item_price = list(items)[item]
            item_weight = items[item_price]
            for capacity in range(1, maxCap):
                if item_weight <= capacit
                    dpt[item][capacity] = max(items[item_weight] + dpt[item-1][capacity-item_weight], dpt[item-1][capacity])
        """
    #print(np.matrix(dpt))



    write_file("results.txt")


if __name__ == '__main__':
    main()