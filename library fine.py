#library fine
def library(d1,m1,y1,d2,m2,y2):
    if y2<y1 and m2:
        return 10000
    elif y1<y2:
        return 0
    elif m2<m1:
        return 500*(m1-m2)
    elif m1<m2:
        return 0
    elif d2<d1:
        return 15*(d1-d2)
    
    
    elif d1<d2:
        return 0





a,b,c=2,7,1014
d,e,f=1,1,1015
print(library(a,b,c,d,e,f))