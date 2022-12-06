#parallel processing
def minTime(files, numCores, limit):
    # Write your code here
    a= []
    b = []
    for i in files:
        if i % numCores == 0:
            a.append(i)
        else:
            b.append(i)
    a.sort(reverse=True)
    return (sum(a[:limit]) // numCores) + sum(a[limit:]) + sum(b)
files=[5,1,3]
num=5
limit=5
print(minTime(files,num,limit))