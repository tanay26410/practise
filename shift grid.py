#shift grid
def shiftgrid(grid,k):
    m=len(grid)
    n=len(grid[0])
    d = m*n
    ans = [[0] * n for i in range(m)]

    start = d - k
    for i in range(m):
        for j in range(n):
                    start %= d
                    r = start // n
                    c = start % n
                    ans[i][j] = grid[r][c]
                    start += 1
    return ans
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(shiftgrid(grid,k))