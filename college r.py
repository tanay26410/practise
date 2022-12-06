# college r
y, z = [int(i) for i in input().split()]
cl = [0] + [int(i) for i in input().split()]
cut = [-1] + [-1 for i in range(y)]
pr = set()
l = []
for i in range(z):
    a, p, q, r, s = input().split(",")
    a = int(a[8:])
    p = float(p)
    q = int(q[2:])
    r = int(r[2:])
    s = int(s[2:])
    l.append([p, a, 1, q])
    l.append([p, a, 2, r])
    l.append([p, a, 3, s])
l.sort(key=lambda x: (-x[0], x[1], x[2]))

for i in l:
    if i[1] not in pr:
        if cl[i[3]] > 0:
            cl[i[3]] -= 1
            cut[i[3]] = i[0]
            pr.add(i[1])
cl = [[cl[i], i, cut[i]] for i in range(1, len(cl))]
cl.sort(key=lambda x:(-x[0], x[1], x[2]))
s = 0
for i in l:
    if i[1] not in pr:
        while s < len(cl) and cl[s][0] <= 0:
            s += 1
        if s < len(cl):
            cl[s][0] -= 1
            if cl[s][2] == -1:
                cl[s][2] = 100
            cl[s][2] = min(cl[s][2], i[0])
            pr.add(i[1])
cl.sort(key=lambda x:-x[2])

for i in cl:
    if i[2] != -1:
        print("C-" + str(i[1]), i[2])
    else:
        print("C-" + str(i[1]), "n/a")