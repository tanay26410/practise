# picking numbers

def pickingNumbers(l):
    maximum=0
    for i in l:
        c=l.count(i)
        d=l.count(i-1)
        c=c+d
        if c > maximum:
            maximum=c
    print(maximum)

a=[1,1,2,2,4,4,5,5,5]
pickingNumbers(a)
