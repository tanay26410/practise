#last stone weight
def stone(s):
    s.sort()
    while len(s)>1:
        s.append(abs(s.pop()-s.pop()))
        
    return s

s=[2,7,4,1,8,1]
print(stone(s))