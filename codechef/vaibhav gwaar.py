#vaibhav gwaar
s=input()
if s[-1].isalpha():
    n=str(len(s))
elif s[-1].isnumeric():
    n=str(len(s[0:-1]))
print(n[-1])