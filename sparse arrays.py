strings=['aba','baba','aba','xzxb']
queries=['aba','xzxb','ab']
res=[]
for i in queries:
    count=0
    for j in strings:
        if i==j:
            count+=1
    res.append(count)
print(res)