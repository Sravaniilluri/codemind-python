n=int(input())
l=list(map(int,input().split()))
m=set(l)
sum=0
for i in m:
    if (i%2==0):
        sum+=i
print(sum)