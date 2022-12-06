#non divisible subset
def divisible(k,s):
    s=set(s)
    max=0
    count=0
    for i in s:
        for j in s:
            if (i+j)%k!=:
                count+=1
                
    
s=[19,10,12,10,24,25,22]
k=4
print(divisible(k,s))