#highest value palindrome
def highestvaluepalindrome(s,n,k):
    li=[]
    li.extend(s)
    x=li[::-1]
    m=0
    
    for i in range(n):
            if li[i]!=li.reverse() and m<k:
                if li[i]>max(li) and li[i]>x[i]:
                    pass
                elif (li[i]<max(li) and li[i]>x[i]):
                    li[i]=max(li)
                    m+=1
                else:
                    li[i]=x[i]
                    m+=1
    return ''.join(li)
s='1234'
n=4
k=1
res=highestvaluepalindrome(s,n,k)
print(res)


