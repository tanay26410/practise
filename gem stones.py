#gem stones
def gemstones(arr):
    g=set(arr[0])
    for i in arr[1:]:
        g=g.intersection(set(i)) 
        
    
    return len(g)
arr = ['abcdde', 'baccd', 'eeabg']
print(gemstones(arr))















