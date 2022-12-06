#longest valid parantheses
def para(s):
    if len(s)==0:
        return 0
    l=count=0
    r=1
    while r!=len(s):
        if s[l]=='(' and s[r]!=')':
            count+=1
        r+=1
        l+=1
    return count*2


s='(()'
print(para(s))