 #zip function


# u=['u1','u2','k']
# n=['h','j']
# print(list(zip(u,n)))
# l=[[1,2],[3,4],[5,6],[7,8]]
# print(list(zip(*l)))
# l1=[1,3,5,7]
# l2=[2,4,6,8]
# new_list=[]
# for i in zip(l1,l2):
#     new_list.append(max(i))
# print(new_list)

def avg(*args):
    li=[]
    for i in zip(*args):
        li.append(sum(i)/len(i))
    return li
l1=[1,3,5,7]
l2=[2,4,5,6]
l3=[4,5,6,7]
l=[[1,3,5,7],[2,4,5,6],[4,5,6,7]]
avg2=lambda *args:[sum(i)/len(i) for i in zip(*args)]
print(avg2(*l))









