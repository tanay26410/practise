#password decryption
def depcryt(s):
    
    s=list(s)
    i=0
    while i < len(s) and s[i].isdigit() and s[i] != "0":
        i+=1
    li=[l for l in range(i, len(s)) if s[l] == "0"]
    for j,k in enumerate(li):
        s[k]=s[i-j-1]
    for j in range(i, len(s)):
        if s[j]=="*":
            s[j-1],s[j-2]=s[j-2],s[j-1]
    return "".join(s[i:]).replace("*", "")
s='51Pa*0Lp*0e'
print(depcryt(s))