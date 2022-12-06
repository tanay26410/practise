#sequence equation
def permutationEquation(p):
    # Write your code here
    a=[]
    for i in p:
        a.append(i-1)
    l=[]
    for j in range(len(p)):
        l.append(a.index(a.index(j)))
    for j in l:
        print(j+1)
    return
q=[5,2,1,3,4]
res=permutationEquation(q)
print(res)