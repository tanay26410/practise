#any and all
# num=[2,4,6,8]
# eve=[True if i%2==0 else False for i in num]
# even=all([True if i%2==0 else False for i in num])
# print(even)
# print(eve)
# eve=any([True if i%2==0 else False for i in num])
# print(eve)
def mysum(*args):
    if all((type(i)==int or type(i)==float) for i in args):
        total=0
        for i in args:
            total+=i
        return total
    return ("wrong input")
print(mysum(1,2,3,4))