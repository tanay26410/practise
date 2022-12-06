#funnystirng
def funnyString(s):
    # Write your code here
    asc=[]
    for i in s:
        asc.append(ord(i))
    d=[]
    count=0
    for i in range(1,len(asc)):
        d.append(abs(asc[i-1]-asc[i]))
    if (d==d[::-1]):
        count+=1
    if count>=1:
        return 'Funny'
    else:
        return 'Not Funny'
s='ivvkx' 

print(funnyString(s))