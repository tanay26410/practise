def rightRotate(li, n):
    o= []
    for i in range(len(li) - n, len(li)):
        o.append(li[i])  
    for i in range(0, len(li) - n): 
        o.append(li[i])      
    return o
k=2
li=[1, 2, 3, 4, 5, 6]
print(rightRotate(li, k))