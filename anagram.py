#anagram
def anagram(s):
    s2=s[len(s)//2:]
    s1=s[:len(s)//2]
    print(s1)
    print(s2)
    count=0
    if len(s1)!=len(s2):
        return -1
    for i in s1:
        if i in s2:
            s2=s2.replace(i,'',1)
    return len(s1)        
s='fdhlvosfpafhalll'
print(anagram(s))
