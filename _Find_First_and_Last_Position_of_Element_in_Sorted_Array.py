n=int(input())
l=list(map(int,input().split()))
a=int(input())
b=[]
for i in range(len(l)):
    if l[i]==a:
        b.append(i)
if len(b)>0:
    print(b[0],b[-1])
else:
    print(-1,-1)