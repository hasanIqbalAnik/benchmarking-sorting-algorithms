from utils import generate_samples, get_numbers_list

bucket = {}


# creating bucket for each digits
def reset_bucket():
    global bucket
    for i in xrange(10): bucket[i] = []


# to handle variable length items`
def radix_group_numbers(numbers):
    joined = []
    max_length = max(len(str(x)) for x in numbers)
    bkt = {}
    for i in xrange(max_length + 1):
        bkt[i] = []
    for item in numbers:
        bkt[len(str(item))].append(item)

    for k, v in bkt.items():
        if v: joined.extend(radix_sort(v))

    return joined


def put_in_buckets(numbers, index):  # assuming that the numbers are of equal lenght
    global bucket
    try:
        for item in numbers:
            c = str(item)[index]
            if c is '0':
                bucket[0].append(item)
            elif c is '1':
                bucket[1].append(item)
            elif c is '2':
                bucket[2].append(item)
            elif c is '3':
                bucket[3].append(item)
            elif c is '4':
                bucket[4].append(item)
            elif c is '5':
                bucket[5].append(item)
            elif c is '6':
                bucket[6].append(item)
            elif c is '7':
                bucket[7].append(item)
            elif c is '8':
                bucket[8].append(item)
            elif c is '9':
                bucket[9].append(item)
    except IndexError:
        print 'error occured'
        print numbers, index


def radix_sort(lst):
    global bucket
    max_length = max(len(str(x)) for x in lst)
    for i in xrange(max_length):
        reset_bucket()
        put_in_buckets(lst, max_length - i - 1)
        lst = []
        for key, value in bucket.iteritems():
            if value is not None:
                for item in value:
                    lst.append(item)
        bucket.clear()
    return lst
