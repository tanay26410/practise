#advance max and min
# def func(i):
#     return len(i)
# func1=lambda a:len(a)
# name=['abc','defg','ab']
# print(min(name,key=func1))
# print(func1)
# def func(item):
#     return item.get('s')
# def func(item):
#     return student[item]['a']
# student={
#      'harshit':{'s':90,'a':24},
#      'm':{'s':75,'a':19},
#      'r':{'s':76,'a':23}
#  }
# print(min(student,key=func))
# print(min(student,key=lambda item: student[item]['a']))
# student1=[
#       {'n':'harshit','s':90,'a':24},
#       {'n':'m','s':75,'a':19},
#       {'n':'r','s':76,'a':23}
#   ]
# print(min(student1,key=func))
# print(max(student1,key=lambda item:item.get('s'))['n'])
gui=[
    {'m':'y','p':84},
    {'m':'fa','p':85},
    {'m':'fd','p':88},
    {'m':'ya','p':848} 
    
]
print(max(gui,key=lambda i:i.get('p')))