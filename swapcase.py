s="Tanay"
sc=""
for i in range(len(s)):
    if s[i]==s[i].upper():
        t=s[i].lower()
        sc+=t
    else:
        t=s[i].upper()
        sc+=t
print(sc)
