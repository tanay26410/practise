def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
    
f=sum(8)
print(f)

