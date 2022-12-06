# char counter
from itertools import count


def charcounter(s):
    c={}
    for char in s:
        c[char]=s.count(char)
    return c
print(charcounter("Tanay"))