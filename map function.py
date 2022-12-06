#map function
# def s(a):
#     return a**2
# n=[1,2,3]
# sq=list(map(s,n))
n=[1,2,3]
# sq=list(map(lambda a:a**2,n))
# print(sq)
# sq=[a**2 for a in sq]
# print(sq)
# sq=[]
# for i in n:
#     sq.append(i**2)
# print(sq)
n=['ab','abc','abcd']
# l=list(map(len,n))
# print(l)
length=map(len,n)
for i in length:
    print(i)