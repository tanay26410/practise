# create dict
d={}
name,age=input("enter name and age :").split()
favmoveis=input('enter your movies :').split(',')
favtunes=input('enter tune :').split(',')
d['name']=name
d['age']=age
d['favmoveis']=favmoveis
d['favtunes']=favtunes
print(d)
for key,values in d.items():
    print(f"key is {key} having value : {values}")