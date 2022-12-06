#reduced string
from queue import Empty
from re import L
import string
def reducedstring(s):
    s=list(s)
    a=''
    i=0
    while len(s)-2>=i:
        if s[i]==s[i+1]:
            del s[i]
            del s[i]
            i=0
        elif s[i]!=s[i+1]:
            i+=1

   
    if s==[]:
        return ('Empty String') 
    else:
        return (''.join(s))
s='txxmubonuhlaryeuujgftedrmmhmaadxrplneqpwhsketqicdpqlecluydmgykrubgmpwfqviabkjoiqdftbbwwgiuudmgrdbkrr'
print(reducedstring(s))