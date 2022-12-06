def Fibonacci(n):
    if n<=1:
        return n
    first=Fibonacci(n-1) 
    second=Fibonacci(n-2)
    return first+second
print(Fibonacci(9))
 