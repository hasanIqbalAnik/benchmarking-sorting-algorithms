from utils import get_numbers_list


def selection_sort(unsorted_lst):
    for k in xrange(len(unsorted_lst) - 1):  # at max this much iteration required to fully sort

        current_minimum = unsorted_lst[k]  # first elem as the current minimum
        current_minimum_idx = k

        for i in xrange(k, len(unsorted_lst), 1):
            if current_minimum > unsorted_lst[i]:
                current_minimum = unsorted_lst[i]
                current_minimum_idx = i
        # swap the current minimum with the kth element
        tmp = unsorted_lst[k]
        unsorted_lst[k] = current_minimum
        unsorted_lst[current_minimum_idx] = tmp
    return unsorted_lst
