# advance sort
gui=[
     {'m':'y','p':84},
     {'m':'fa','p':85},
     {'m':'fd','p':88},
    {'m':'ya','p':848} 
    
]
print(sorted(gui,key=lambda i:i.get('p')))
print(sorted(gui,key=lambda i:i.get('p'),reverse=True))
# student={
#       'harshit':{'s':90,'a':24},
#       'mohit':{'s':75,'a':19},
#       'rohit':{'s':76,'a':23}
# }
# print(sorted(student,key=lambda i:student[i]['a']))
# print(sorted(student,key=lambda i:student[i]['a'],reverse=True))