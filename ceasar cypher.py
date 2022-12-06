#ceasar cypher
from heapq import nsmallest


def ceasar(s,k):
    rs=list(s)
    ns=[]
    for i in rs:
        z=ord(i)
        if z+k>=97 and z+k<=122:
                if (z+k)>122:
                    ns.append(chr(96+(z+k-122)))
                else:
                    ns.append(chr(z+k))
        elif  (z>=65 and z<=90) :
                if (z+k)>90:
                    ns.append(64+(z+k-90))
                else:
                    ns.append(chr(z+k))
        else:
             ns.append(i)
    return (''.join([x for x in ns]))
s='Hello_World!'
k=2
print(ceasar(s,k))