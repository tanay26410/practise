#input and output
n,k=map(int,input().split())
n=list(map(int,input().split(',')))[:n]
count=0
for i in n:
    if i%k==0:
        count+=1
print(count)
