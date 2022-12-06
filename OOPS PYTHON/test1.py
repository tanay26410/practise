def reverse(l):
    result=[]
    a=""
    for i in l:
        a=i[::-1]
        result.append(a)
    return result
l=['abc','def','ghi']
print(reverse(l))