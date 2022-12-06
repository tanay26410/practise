def f(n):
    if n<0:
        return -1*f(-1*n)
    elif n==0:
        return 0
    else:
        return 4+f(n-1)
print(f(9))
