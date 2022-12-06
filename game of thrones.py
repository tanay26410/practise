#game of thrones
no_chars=256
def gameOfThrones(s):
    cout=[0]*no_chars
    for i in range(0, len(s)):
        cout[ord(s[i])] = cout[ord(s[i])] + 1

    odd = 0
    for i in range(0,len(cout)):
        if (cout[i] & 1):
            odd = odd + 1
        if (odd > 1):
            return 'NO'
    return "YES"
s='aaabbbb'
res=gameOfThrones(s)
print(res)