#save the prisoner
def savetheprisoner(n,m,s):
    r=m%n
    if (r+s-1)%n==0:
        return n
    return (r+s-1)%n
n=4
m=6
s=2
res=savetheprisoner(n,m,s)
print(res)
