from utils import get_numbers_list

def bubble_sort(lst):
    max_iter = len(lst)
    counter = 0
    for m in xrange(max_iter):
        for i in xrange(max_iter - 1 - counter):  # -counter to execute faster
            if lst[i] > lst[i + 1]:  # should swap
                tmp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = tmp
        counter += 1

    return lst
