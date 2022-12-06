#finding the median
import bisect
def median(a):
    n=len(a)
    z=[]
    r=0
    l1=[]
    b=0
    for i in range(n):
        b=b+1
        bisect.insort(z,a[i])
        if b==1:
            l1.append(float(z[0]))
        elif b%2==0:
            r=b//2
            # z.pop()
            l1.append((z[r-1]+z[r])/2)
            # print(r)
        else:
            # z.pop()
            l1.append(float(z[b//2]))
    return l1
    # r=0
    # for i in range(n):
    #     z.insert(0,a.pop(0))
    #     z.sort()
    #     if len(z)==1:
    #         print(float(z[0]))
    #     elif len(z)%2==0:
    #         r=len(z)//2
    #         # z.pop()
    #         print((z[r-1]+z[r])/2)
    #         # print(r)
    #     else:
    #         # z.pop()
    #         print(float(z[len(z)//2]))
            
            

n = 6
a = [12, 4, 5, 3, 8, 7]
print(median(a))
