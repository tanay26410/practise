def dayOfProgrammer(year):
    # Write your code here
    if(year=="1918"):
        return("26.09."+str((year)))
    elif((year%4==0 and year%100!=0)or(year%400==0)):
        return("12.09."+str(year))
    else:
        return("13.09."+str(year))
result=dayOfProgrammer(1800)
print(result)