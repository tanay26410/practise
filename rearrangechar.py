#rearrangechar
from collections import defaultdict
import heapq
def rearrangeString(self, str):
        #code here
        d=defaultdict(int)
        for i in str:
            d[i]+=1
        a=[]
        for i,j in d.items():
            heapq.heappush(a,[(-j),i])
        p=[0]
        rs=''
        while a:
            temp=heapq.heappop(a)
            rs+=temp[1]
            temp[0]+=1
            if p[0]<0:
                heapq.heappush(a,p)
            p=temp
        if len(rs)==len(str):
            return rs
        else:
            return "-1"