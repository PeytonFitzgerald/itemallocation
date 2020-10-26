def insertion_sort(array):
    """
    Uses an insertion sort algorithim to sort a given array.
    :param array: Array to be sorted
    :return: Sorted array
    """
    """
    array_length = int(len(array))
    for i in range(1,array_length):
        current_value = array[i].start
        comparison_index = i - 1
        cur_activity = array[i]
        cur_start = cur_activity.start
        prev_start = prev_activity.start
        while comparison_index >= 0:
            if cur_start > prev_start:
                prev_activity = array[comparison_index]
                previous = prev_activity
                array[comparison_index] = cur_activity
                array[comparison_index+1] = previous
                comparison_index -= 1
            else:
                break

    return array
    """

    array_length = int(len(array))
    for i in range(1,array_length):
        # get current, compare to left. If bigger, switch
        current_activity = array[i]
        current_value = current_activity.start
        comparison_index = i - 1
        while comparison_index >= 0:
            if int(current_value) >= int(array[comparison_index].start):
                previous = array[comparison_index]
                array[comparison_index] = current_activity
                array[comparison_index+1] = previous
                comparison_index -= 1
            else:
                break

    return array


def merge_sort(array):
    """
    Uses a merge sort algorithim to sort a given array.
    :param array: Array to be sorted
    :return: Sorted array
    """
    # take an array, find mid point, split it into two halves
    array_length = len(array)
    # base case
    if array_length <= 1:
        return array
        # if length is 1, current array is sorted
    # split routine
    mid_point = int(array_length / 2)

    left_array = merge_sort(array[:mid_point])  # recursive call for left half of array until we can't split anymore on
                                                # the left.
    right_array = merge_sort(array[mid_point:]) # If we can't split the left side,  we recursively call the right until
                                                # we can split on the left. Otherwise split until we can't split anymore
                                                # on the right
    return merge(left_array, right_array)


def merge(left_array, right_array):
    """
    Merge routine of the merge sort algorithim - sorts and merges left and right halves of the array.
    :param left_array:
    :param right_array:
    :return: the merged array
    """
    new_array = []
    i = 0
    k = 0
    while i < len(left_array) and k < len(right_array): # append until one of the halves is empty
        if int(left_array[i].start) < int(right_array[k].start):
            # if left is bigger than right, append right and move forward one
            new_array.append(right_array[k])
            k += 1
        else:
            # if right is bigger than left, append left and move forward one
            new_array.append(left_array[i])
            i += 1
    # merge two halves into new array. Don't know which is empty, so do both.
    new_array += right_array[k:]
    new_array += left_array[i:]

    return new_array

class ActivityClass:
    def __init__(self, num, start, end):
        self.num = num
        self.start = start
        self.end = end

    def get_num(self):
        return self.num

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end



def read_file(name):
    with open(name, 'r') as datafile:
        lines = datafile.read().splitlines()
    i = 0
    all_sets = []
    set_num = 0
    while i < len(lines):
        # get number of activities for this set of activities
        num_activities = int(lines[i])
        all_sets.append([])
        all_sets[set_num] = [num_activities, []]
        i+=1

        # store info about each activity in this set
        for n in range(num_activities):

            cur_line_info = lines[i].split()  # act_info[0] is activity number, act_info[1] is start, act_info[2] is end
            num = cur_line_info[0]
            start = cur_line_info[1]
            end = cur_line_info[2]
            # create obj, add to our list
            act_obj = ActivityClass(num, start, end)
            all_sets[set_num][1].append(act_obj)
            i += 1  # increment to recognize we're moving to next line

        set_num += 1
    return all_sets


def main():

    data_list = read_file('act.txt')
    set_num = 1

    for activity_set in data_list:
        num_activities = activity_set[0]
        sorted_activity_list = merge_sort(activity_set[1])
        opt_set = [sorted_activity_list[0]]
        i = 1
        opt_index = 0

        # starting from last activity to start, choose all subsequent activities based on
        # whether their end time is compatible with the latest activity added to our optimal set's start time
        while i <= (len(sorted_activity_list)-1):
            cur_opt = opt_set[opt_index]
            pot_opt = sorted_activity_list[i]
            if int(pot_opt.end) <= int(cur_opt.start):
                opt_set.append(sorted_activity_list[i])
                opt_index += 1
            i += 1


        print('Set ' + str(set_num))
        print('Number of activities selected = ' + str(len(opt_set)))
        print('Activities:', end=' ')
        for act in opt_set:
            print(act.num, end=' ')
        set_num += 1
        print('\n')


if __name__ == '__main__':
    main()

