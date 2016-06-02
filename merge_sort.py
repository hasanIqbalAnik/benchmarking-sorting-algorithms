# merge two lists

class stack:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def __str__(self):
        return str(self.items)

    def empty(self):
        return len(self.items) is 0

    def reverse(self):
        l = []
        while self.empty() is False:
            l.append(self.items.pop())
        return l


def merge(l1, l2):  # takes two sorted lists and merges them while keeping the order
    ll = []  # long list consists of l1 + l2
    l1.reverse()
    l2.reverse()
    st1 = stack(l1)
    st2 = stack(l2)
    while st1.empty() is False and st2.empty() is False:
        i1 = st1.peek()
        i2 = st2.peek()
        if i1 <= i2:
            ll.append(i1)
            l1.pop()
        else:
            ll.append(i2)
            l2.pop()
    if st1.empty() is True and st2.empty() is False:
        ll = ll + st2.reverse()
    elif st2.empty() is True and st1.empty() is False:
        ll = ll + st1.reverse()

    return ll


def merge_sort(lst):
    if len(lst) is 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)
