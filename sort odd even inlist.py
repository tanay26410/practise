def sortoe(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    return [odd,even]
print(sortoe([1,2,3,4,5,6,7,8,9]))