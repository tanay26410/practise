#watering plants
def wateringplants(plants,capacity):
    c=0
    t=capacity
    for i in range(len(plants)):
            if plants[i]<=t:
                c+=1
                t-=plants[i]
            else:
                c+=i+i+1
                t=capacity
                t-=plants[i]
    return c
    
arr=[2,2,3,3]
a=5
print(wateringplants(arr,a))