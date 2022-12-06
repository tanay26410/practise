#jumping clouds
def jumpingonclouds(c):
    co=i=0
    while i<len(c)-2:
        if c[i]==1:
            i+=1
        else:
            i+=2
        co+=1
    if i<len(c)-2:
        co+=1
    return co

        

                
    
c=[0, 0, 1 ,0, 0, 0, 0 ,1, 0 ,0]
res=jumpingonclouds(c)
print(res)