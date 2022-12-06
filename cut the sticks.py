#cut the sticks
def cutthesticks(arr):
    count=0
    l=[0]*len(arr)
    # while arr!=[0]*len(arr):
    #     for i in arr:
    #         if i!=0:
    #             count+=1
    #     l.append(count)
    #     arr=[x-min(arr) for x in arr]
    #     while 0 in arr:
    #         arr.remove(arr)
    return l
arr=[5,4,4,2,2,8]
res=cutthesticks(arr)
print(res)
        