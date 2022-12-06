#tathagat capgemini1
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
sum=0
for i in range(n):
    sum=+min(arr)
    mi=arr.index(min(arr))
    arr.pop(mi-1)
    arr.pop(mi)
    arr.pop(mi+1)
    
print(arr)

