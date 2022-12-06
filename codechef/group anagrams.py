#group anagrams
from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
def grpana(s):
    d=defaultdict(list)
    for i in s:
        d[tuple(i)].append(i)
    return list(d.values())
print(grpana(strs))