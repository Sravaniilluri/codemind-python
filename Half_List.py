n=int(input())
l=list(map(int,input().split()))
m=n//2-1
n=n//2
c=l[:m:-1]
b=l[:n:]
a=c+b
print(*a)