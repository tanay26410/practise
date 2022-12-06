# args power
def power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return("no list passed")
li=[3,2,3,4]
print(power(3,*li))