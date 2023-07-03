n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in l:
    if i not in a and l.count(i)==i:
        a.append(i)
        c+=1
print(c)