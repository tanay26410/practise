#spiral matirx
def spiral(n):
    ans = [[0 for i in range(n)] for j in range(n)]

    l, r, t, b, n = 0, n - 1, 0, n - 1, 1

    while l <= r and t <= b:
            for j in range(l, r + 1):
                ans[t][j] = n
                n += 1
            for i in range(t + 1, b):
                ans[i][r] = n
                n += 1
            for j in reversed(range(l, r + 1)):
                if t < b:
                    ans[b][j] = n
                    n += 1
            for i in reversed(range(t + 1, b)):
                if l < r:
                    ans[i][l] = n
                    n += 1
            l, r, t, b = l + 1, r - 1, t + 1, b - 1

    return  ans
n=3
print(spiral(n))
