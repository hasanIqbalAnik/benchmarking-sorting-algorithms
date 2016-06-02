import time

from utils import generate_samples, get_numbers_list
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from radix_sort import radix_sort, radix_group_numbers
from selection_sort import selection_sort

#first we need to generate a hugh amount of data

generate_samples(100000)

lst = get_numbers_list('data.txt')

start_time = time.time()
radix_group_numbers(lst)
end_time = time.time()

print 'radix sort took', end_time - start_time, 'seconds'


start_time = time.time()
merge_sort(lst)
end_time = time.time()

print 'merge sort took', end_time - start_time, 'seconds'


start_time = time.time()
bubble_sort(lst)
end_time = time.time()

print 'bubble sort took', end_time - start_time, 'seconds'


start_time = time.time()
selection_sort(lst)
end_time = time.time()

print 'selection sort took', end_time - start_time, 'seconds'



