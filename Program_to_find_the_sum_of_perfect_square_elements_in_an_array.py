n=(input())
l=list(map(int,input().split()))
m=max(l)
c=0
for i in range(m):
    i=i*(i)
    if i in l:
        c=c+i
print(c)
    
    