#move zero to end
def move(nums):
    for i in range(0,len(nums)):
        if nums[i]==0:
            nums.remove(0)
            nums.append(0)
    return nums
nums=[0,0,1]
print(move(nums))