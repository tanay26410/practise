array=['a','a','b','d','b','c']
freqdict={}
for element in array:
    if element in freqdict:
        freqdict[element]+=1
    else:
        freqdict[element]=1
for element in freqdict:
    if freqdict[element]==1:
         print(element)
         break          

