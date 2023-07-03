n=int(input())
m=int(input())
row=[0 for i in range(n)]
a=[row.copy() for i in range(m)]
s=0
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(m):
        s+=l[j]
print(s)