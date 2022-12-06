#numbers to str
def convert(li):
    new=[str(i) for i in li if (type(i)==int or type(i)==float)]

    return new
li=['a','b',[1,2,3],1,2,3,3.4,0.1,]
print(convert(li))