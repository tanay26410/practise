#counting valley
def countingValleys(steps, path):
    sealevel=valley=0
    for i in path:
        if i=='U':
            sealevel+=1
        else:
            sealevel-=1
        if i=='U' and sealevel==0:
            valley+=1
    return valley
steps=8
path='UDDDUDUU'
res=countingValleys(steps,path)
print(res)