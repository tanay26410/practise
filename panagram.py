#panagram
def pangram(s):
    s=s.replace(' ','')
    s=s.lower()
    a=list()
    for i in s:
        a.append(i)
    a=set(a)
    if len(a)==26:
        return 'pangram'
    return 'not pangram'

s='We promptly judged antique ivory buckles for the next prize'
print(pangram(s))