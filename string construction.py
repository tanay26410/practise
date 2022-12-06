#srinng construction
def stringConstruction(s):
    p=''
    for i in s:
        if i not in p:
            p+=i
            s=s.replace(i,'',1)
    if p==s:
        return len(p)
    return len(p)