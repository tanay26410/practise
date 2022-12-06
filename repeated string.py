#repeated string
def repeatedstring(s,n):
    a=n//len(s)
    b=n%len(s)
    c=(s.count('a'))*a
    d=s[:b].count('a')
    return c+d
s='x'
n=100
print(repeatedstring(s,n))