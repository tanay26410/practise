#permutations 2
from itertools import permutations


def perm(s):
    perm=permutations(s)
    li=[]
    for i in perm:
        if list(i) not in li:
            li.append(list(i))
    return li

s=[1,1,2]
print(perm(s))