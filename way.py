n=int(input())
for i in range(n):
    a=input()
    y=len(a)
    if len(a)>10:
        c=a[0]+str(y-2)+a[y-1]
        print(c)
    else:
        print(a)