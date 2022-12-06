#list kargs
def lis(li,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title()for name in li]
    else:
        return[name.title() for name in li]
name=["harshit","tanay"]
print(lis(name,reverse_str=True))