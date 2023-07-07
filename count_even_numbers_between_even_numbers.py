n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(n):
    if(i==0 or i==n-1):
        continue
    else:
        if(a[i]%2==0):
            if(a[i+1]%2==0 and a[i-1]%2==0):
                c+=1
print(c)