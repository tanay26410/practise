#alternating character
def alternating(s):
    count=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            count+=1
    return count
s='ABABABAB'
print(alternating(s))