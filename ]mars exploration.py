#mars exploration
def marsExploration(s):
    count=0
    x=0
    li=[]
    for i in range(3,len(s)+1,3):
        if (s[x:i])!="SOS":
            li.append(s[x:i])
        x=i
    for i in li:
        if i[0]!='S':count+=1
        if i[1]!='O':count+=1
        if i[2]!='S':count+=1
    return count
s='SOSOOSOSOSOSOSSOSOSOSOSOSOS'
# s='SOSSPSSQSSOR'
# s='SOSSOT'
print(marsExploration(s))