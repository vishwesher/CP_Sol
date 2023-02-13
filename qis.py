n=int(input())
l=list(map(int,input().split()))
mm=max(l)
x=l.index(max(l))
for j in range(x,0,-1):
            temp=l[j]
            l[j]=l[j-1]
            l[j-1]=temp
m=min(l)
l=l[::-1]
y=l.index(min(l))
print(x+y)