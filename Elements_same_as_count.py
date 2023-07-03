n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a and l.count(i)==i:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    print(*a)