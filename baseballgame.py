#baseballgame
def base(ops):
    li=[]
    for i in ops:
        if i:
            li.append(int(i))
            print(li)
            
        else:
            if i=='C':
                li.pop()
            if i=='D':
                li.append(2*li.pop())
                
            if i=='+':
                li.append(li[-2]+li[-1])
            
    return sum(li)
li=["5","-2","4","C","D","9","+","+"]
ans=base(li)
print(ans)
