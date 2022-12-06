# Group the People Given the Group Size They Belong To
from collections import defaultdict
def group(gs):
    d=defaultdict(list)
    for i in range(len(gs)):
        d[gs[i]].append(i)
    return d
gs=[3,3,3,3,3,1,3]
print(group(gs))
