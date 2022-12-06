#jesse and cookies
import heapq
def cookies(k, A):
    count=0
    heapq.heapify(A)
    while A[0]<k and len(A)!=1:
        heapq.heappush(A,heapq.heappop(A)+2*heapq.heappop(A))
        count+=1
    if A[0]>k:
        return count
    else:
        return -1
    # if len(l)==0: return 0    
    # for i in range(len(l)):
    #     l.sort()
    #     a=l.pop(l.index(min(l)))
    #     b=l.pop(l.index(min(l)))
    #     if a and b <9:
    #         z=a+2*b
    #         l.append(z)
    #         count+=1
    #     else: break

    # if l[0]>k:
    #     return(count)
    # else:
    #     return(-1)      

A = [13,47,74,12,89,74,18,38]
k=90
res=cookies(k,A)
print(res)
