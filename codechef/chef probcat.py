#chef probcat
t=int(input())
for i in range(t):
    x=int(input())
    if 1<=x and x<100:
        out='Easy'
    elif 100<=x and x<200:
        out='Medium'
    else:
        out='Hard'
    print(out)