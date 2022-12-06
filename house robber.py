#house robber
def house(nums):
    sum1=[]
    sum2=[]
    for i in range(len(nums)):
        if i%2==0:
            sum2.append(nums[i])
        else:sum1.append(nums[i])
    return max(sum(sum1),sum(sum2))
nums=list(map(int,input().strip().split()))
print(house(nums))