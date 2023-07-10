n=int(input())
for i in range(n):
    s=input()
    for j in range(len(s)):
        if s[j] in '1234567890':
            print("Yes")
            break
    else:
        print("No")