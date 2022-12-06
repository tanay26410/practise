#balanced bracket
def isBalanced(s):
    # Write your code here
    n=-1
    while(len(s)!=n):
        n=len(s)
        s=s.replace('{}','')
        s=s.replace('[]','')
        s=s.replace('()','')
    if (len(s)==0):
        return 'YES'
    else: return "NO"
s = '{[()]}'
res=isBalanced(s)
print(res)