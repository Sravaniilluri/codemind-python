n,m=map(int,input().split())
row=[0 for i in range(n)]
a=[row.copy() for i in range(m)]
sum=0
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(m):
        sum+=l[j]
print(sum)