def perfect_check(num):
    list = []
    for i in range(1,num):
        if (num%i==0):
            list.append(i)
    if (sum(list)==num):
        print("{} is a perfect number".format(num))
    else:
        print("{} is not a perfect number".format(num))
num = 6
print(perfect_check(num))
