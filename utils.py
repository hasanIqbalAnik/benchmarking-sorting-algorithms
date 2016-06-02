import sys
import random

# n is the number of samples generated
def generate_samples(n):
    lst = []
    while(n > 0):
        lst.append(random.randint(0, 1000000)) #random integer between 0 and a million
        n -= 1
    f = open("data.txt", "w+")
    for item in lst:
        f.write(str(item) + " ")
    f.close()
    print 'samples written at data.txt...'

def get_numbers_list(fname):
    num_arr = []
    f = open(fname, "r")
    for line in f:
        num_arr.append(list(int(x) for x in line.strip().split(" ")))
    return num_arr[0]