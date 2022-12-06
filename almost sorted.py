#almost sorted


def almostsorted(arr):
    
    l=0
    r=len(arr)-1
    li=[]
    while l<r:
        if arr[l]>arr[r]:
            if arr[l+1]>arr[r-1]:
                li.append(l)
                li.append(r)
                temp=arr[l:r]
                temp.sort()
                arr[l:r]=temp
            else:
                li.append(l)
                li.append(r)
                arr[l],arr[r]=arr[r],arr[l]
            break
        l+=1
        r-=1
    if arr==sorted(arr):
        print('yes')
        print('reverse',li)
        return
    else:
        print('no')
        return
arr=[1,5,4,3,2,]
print(almostsorted(arr))
        

