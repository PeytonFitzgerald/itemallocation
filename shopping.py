import numpy as np

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
            "weights": [],
            "prices": [],
            "capacities": []
            }
        # get # of items and iterate through and store info for this case
        items = int(lines[i])

        i+=1

        for n in range(items):
            item_desc = lines[i].split()    # item_desc[0] is price, #item_info[1] is weight
            case_info["prices"].append(item_desc[0])
            case_info["weights"].append(item_desc[1])
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

    for case in case_list:
        items = case["items"]
        prices = case["prices"]

        family = case["capacities"]
        num_items = len(prices)
        maxCap = get_max_capacity(family)       # highest carrying capacity in family

        # create DPT
        dpt = [[0 for x in range(num_items+1)] for y in range(maxCap+1)]
        row = 0
        for item in range(num_items+1):
            i = row         # index for e asily accessing menu
            row += 1



    write_file("results.txt")


if __name__ == '__main__':
    main()