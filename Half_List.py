s=int(input())
l=list(map(int,input().split()))
m=s//2-1
n=s//2
for i in l:
    a=l[:m:-1]
    b=l[:n:]
    c=a+b
print(*c)