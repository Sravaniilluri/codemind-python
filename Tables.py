n,r=map(int,input().split())
d=[]
for i in range(1,r+1):
    if i%2!=0:
        d.append(i)
        for j in d:
            c=n*j
            
        print(n,"x",j,"=",c)
        