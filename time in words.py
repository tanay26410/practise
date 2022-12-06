#time in words
def timeInWords(h, m):
    # Write your code here
    d={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twentyone',22:'twenty-two',23:'twenty-three',
24:'twenty-four',25:'twenty-five',26:'twenty-six',27:'twenty-seven',28:'twenty-eight',29:'twenty nine'}
    if m==00:
        return d[h]+' o\' clock'
    if m==15:
        return 'quarter past '+d[h]
    if m==45:
        return 'quarter to '+d[h+1]
    if m==30:
        return 'half past '+d[h]
    if m>0 and m<30:
        return d[m]+' minutes past '+d[h]
    if m>30 and m<60:
        return d[60-m]+' minutes to '+d[h+1]
h=6
m=35
print(timeInWords(h,m))