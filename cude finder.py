#cude fincer
def cube(n):
    cube=dict()
    for i in range(1,n+1):
        cube[i]=i**3
    return cube
print(cube(7))
