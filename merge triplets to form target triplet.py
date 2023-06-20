#merge triplets to form target triplet
def mergeTriplets(triplets, target):
        li=[]
        for i in triplets:
            if any(i)==any(target):
                li.append(i)
        
        s=list(s)
        count=0
        for i in target:
             if i in s:
                  count+=1
        if count==len(target):
             return True
        return False
#triplets = [[2,5,3],[1,8,4],[1,7,5]]
#target = [2,7,5]
#triplets = [[3,4,5],[4,5,6]]
#target = [3,2,5]
triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target = [5,5,5]
print(mergeTriplets(triplets,target))