n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,len(l)):
    if (l[i]%2!=0):
        c=i
print(c)
    