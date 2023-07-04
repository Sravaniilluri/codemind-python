n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in l:
    if (k>=i):
        s=s+i
    else:
        break
print(s)
    