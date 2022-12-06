#hackerrank in a substring
def hackerrank(s):
    li={}
    c='hackerrank'
    a='hackernk'
    for i in c:
        if i not in s:
            return 'NO'
    if  s.count('a')<2 or s.count('r')<2  :
        return 'NO'
        
    for i in s:
        if i in c:
            li[i]=s.index(i)
    # li=li.keys()
    # for i,j in zip(li,a):
    #         if i!=j:
    #             return 'NO'
    return li
    
# s='hhaacckkekraraannk'
# s='rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'
s='hereiamstackerrank'
print(hackerrank(s))