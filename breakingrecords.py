def breakingRecords(scores):
    # Write your code here
    sc=scores[0]
    ma=0
    mi=0
    for i in range(len(scores)):
        if scores[i]>sc:
            ma+=1
            sc=scores[i]
    for i in range(len(scores)):
        if sc>scores[i]:
            mi+=1
            sc=scores[i]
    return (ma,mi)
scores=[3,4,21,36,10,28,35,5,24,42]
result=breakingRecords(scores)
print(result)