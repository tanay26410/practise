#chocolate feast
from mmap import mmap


def feat(n,c,m):
    wc=cc=n//c

    while wc >= m:

        cc += wc//m

        wc = wc//m + wc%m
    return cc




n=10
c=2
m=5
print(feat(n,c,m))

