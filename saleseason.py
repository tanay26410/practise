#saleseason
T=int(input())
for _ in range(T):
    X=int(input())
    if X<=100:
        ans=X
    elif 100<X<=1000:
        ans=X-25
    elif 1000<X<=5000:
        ans=X-100
    else:
        ans=X-500
    print(ans)