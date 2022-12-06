def remove(string,word):
    newstr=string.replace(word,"")
    return newstr.strip( )
this="  tanay is good boy                  "
n=remove(this,"good")
print(n) 