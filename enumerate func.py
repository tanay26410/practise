#enumerate func 
# names=['abc','abcdef','harshit']
# for i in range(len(names)):
#     print(f"{i}--->{names[i]}")
# for pos,name in enumerate(names):
#     print(f"{pos}-->{name}")
def index(string,names):
    for pos,name  in enumerate(names):
        if string == name:
            return pos
    return -1

names=['abc','abcdef','abc']
string='harshit'
print(index(string,names))