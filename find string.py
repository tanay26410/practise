#find string
def string(s,k):
    count=0
    for i in range(len(s)):
        if s[i:].startswith(k):
            count+=1
    return count
s='abcdcdc'
k='cdc'
print(string(s,k))