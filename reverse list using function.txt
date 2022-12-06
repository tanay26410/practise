def reverse(l):
    result=[]
    for i in l:
        result=l[::-1]
    return result
l=['abc','def','ghi']
print(reverse(l))