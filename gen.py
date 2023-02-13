n=int(input())
l=list(map(int(),input().split()))
m=max(l)
mi=min(l)
for i in range (n):
    if m == l[i]:
        mp=i
for i in range (n):
    if mi == l[i]:
        mip=i



