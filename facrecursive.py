def factorial(n):
    if n!=1:
        return n*factorial(n-1)
    else:
        return n
    
f=factorial(8)
print(f)

