#marcs cakewalk
def cake(s):
    sum=0
    s.sort(reverse=True)
    print(s)
    for i in range(len(s)):
        sum+=(s[i]*2**i)
    return sum
s=[1,3,2]
print(cake(s))