#cavitymap
def cavity(grid):
    li=[]
    a=[]
    for i in grid:
        a.append(list(i))
    for i in range(1,(len(grid)-1)):
        for j in range(1,(len(grid)-1)):
            if grid[i][j]>max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
                a[i][j]='X'
    for i in a:
        li.append(''.join(i))
    return li


# grid=['989','191','111']
# grid=['1112', '1912', '1892', '1234']
grid=['17323','83521','68656','44424','98855']
print(cavity(grid))