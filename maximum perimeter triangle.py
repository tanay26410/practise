#maximum perimeter triangle
def perimeter(sticks):
    i=len(sticks)-3
    while i>=0 and sticks[i]+sticks[i+1]<=sticks[i+2]:
        i-=1
    if i>=0:
        return sticks[i],sticks[i+1],sticks[i+2]
    return (-1)
                    

                    

# sticks=[1,2,3,4,5,10]
sticks=[1,1,1,3,3]
print(perimeter(sticks))