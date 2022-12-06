s=[5,1,2,4,4,2,4,2,2,5,1,4,3,1,1,1,2,1,4,1]
d=18
m=6
li=0
for i in range(len(s)):
    if sum(s[i:m+i])==d:
        li+=1

print(li)
        

