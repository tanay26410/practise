#closure function or first class fucntion
def to_pow(x):
    def cal_pow(n):
        print (n**x)
    return cal_pow
cube=to_pow(4)
cube(2)