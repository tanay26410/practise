#tathagat capgemini
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
# a=[2,234,22,29,21]
# b=[234,21,29,2]
# c=[234,2,29]
# a=[1,2,3]
# b=[3,2]
# c=[2]
for i in a:
    if i not in b:
        print(i)
for j in b:
    if j not in c:
        print(j)
        