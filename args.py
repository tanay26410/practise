#args 
def add(num,*arg):
    t=0
    for i in arg:
        t+=i
    print(t)
add(1,2,3,4)