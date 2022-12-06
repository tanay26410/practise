#atul bajpai
from itertools import accumulate

n=int(input())
k=int(input())

a=[]
for i in range(n):
        a.append(int(input()))

acc = []

for i in range(n):
            acc.extend(accumulate(a[i:]))

acc.sort()


print(acc[len(acc)-k]%1000000007)