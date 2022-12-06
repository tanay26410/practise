#valid palindrome
def palindrome(s):
    # if s==s[::-1]:
    #         return True
    # li=[]
    # for i in range(len(s)):
    #     li.append(s[:i]+s[i+1:])
    #     # if a==a[::-1]:
    #     #     return True
    # for i in li:
    #     if i==i[::-1]:
    #         return True
    #     else:
    #         return False
    
    h, t = 0, len(s) - 1  
    while h < t:
        if s[h] != s[t]:  
                 return s[h:t] == s[h:t][::-1] or s[h + 1:t + 1] == s[h + 1:t + 1][::-1]
        h, t = h + 1, t - 1
        return True

           
    
s='cbbcc'
print(palindrome((s)))
