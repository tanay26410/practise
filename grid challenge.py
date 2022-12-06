#grid challenge
def gridChallenge(grid):
    # Write your code here
    r=[]
    c=[]
    for i in range(len(grid)):
        temp=[]
        for j in range(len(grid[i])):
            temp.append(grid[i][j])
            temp.sort()
        r.append(temp)
    
    for i in range(len(r[0])):
        temp=[]
        for j in range(len(grid)):
             temp.append(r[j][i])
        c.append(temp)
    for i in c:
        if i!=sorted(i):
             return "NO"
    return "YES"
t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    grid=[]
    for j in range(n):
        wo=input()
        grid.append(wo)
    print(gridChallenge(grid))