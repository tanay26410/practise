#makepalindrome
t=int(input())
for i in range(t):
    n=int(input())
    k=input()
    l=0
    r=len(k)-1
    c=''
    count=0
    while l<r:
        if k[l:r]==k[l:r][::-1]:
            c=k[l:r]
            
        if k[l+1:r]==k[l+1:r][::-1]:
            c=k[l+1:r]
            break
        if k[l+1:r+1]==k[l+1:r+1][::-1]:
            c=l[l+1:r+1]
            break
        if k[l:r+1]==k[l:r+1][::-1]:
            c=l[l:r+1]
            break
        l+=1
        r-=1
    print(c)