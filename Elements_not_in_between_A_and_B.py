n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i not in range(a,b+1):
        c.append(i)
if len(c)==0:
    print("-1")
else:
    print(*c)