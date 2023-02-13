x=input()
n=len(x)

y=0
for i in range(n):
    if((x[i]=='7')or(x[i]=='4')):
        y+=1
if ((y==4) or( y==7)):
    print('YES')
else:
    print('NO')