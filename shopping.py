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
            case_info["capacities"].append(int(lines[i]))
            # do stuff with member
            i += 1

        test_cases[1].append(case_info)

    return test_cases

def write_file(results, case_num):
    print("Test Case " +str(case_num))
    max_value = results[0]
    print("Total Price is " + str(max_value))
    print("Member Items")
    family_list = results[1]
    for i in range(len(family_list)):
        print(str(i) + ": ", end='')
        item_list = family_list[i]
        for item in range(len(item_list)):
            if item_list[item] == 1:
                print(item, end=' ')
        print('\n')
    #with open("shopping.out") as new_file:



def get_max_capacity(weight_list):
    max_capacity = 0
    for capacity in weight_list:
        max_capacity = max(max_capacity, int(capacity))
    return max_capacity

def main():
    max_value = 0
    test_case = read_file("shopping.txt")
    case_list = test_case[1]
    testcase_num = 0
    results_dict = []
    for case in case_list:
        testcase_num += 1
        items = case["items"]
        family = case["capacities"]
        num_items = len(items)
        maxCap = get_max_capacity(family)       # highest carrying capacity in family

        # create dynamic programming table to store all sub-problem results
        dpt = [[0 for x in range(maxCap+1)] for _ in range(num_items+1)]
        row = 0
        for item in items:
            row += 1
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

        print (DataFrame(dpt))
        print ("max $ obtainable is " + str(dpt[row][capacity]))
        case_results = [dpt[row][capacity], []]
        for member in range(len(family)):
            item_list = [0] * (num_items - 1)
            capacity = family[member]
            row = num_items
            max_value += dpt[row][capacity]
            while capacity > 0 and row > 0:
                if dpt[row][capacity] == dpt[row-1][capacity]:
                    row -= 1
                else:
                    cur_item_weight = items[(list(items)[row-1])]
                    item_list[row-2] = 1
                    capacity = capacity - cur_item_weight
                    row -= 1
            case_results[1].append(item_list)
        write_file(case_results, testcase_num)





    #write_file("results.txt")


if __name__ == '__main__':
    main()