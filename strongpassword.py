#strongpassword
def strongpassword(password):
    
    count=0
    if any(x.isdigit() for x in password):
        count+=1
    if any(x.islower() for x in password):
        count+=1
    if any(x.isupper() for x in password):
        count+=1        
    if (x in '@!#$%^&?/`~-_' for x in password):
        count+=1
    return max(count,6-len(password))
s=input()
print(strongpassword(s))