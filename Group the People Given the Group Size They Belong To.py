# Group the People Given the Group Size They Belong To
from collections import defaultdict
def group(gs):
    d=defaultdict(list)
    res=[]
    for i in range(len(gs)):
        res.apprnd(i)
    return res
gs=[3,3,3,3,3,1,3]
print(group(gs))
