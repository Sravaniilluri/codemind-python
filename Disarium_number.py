n = input()
len_n = len(n)
n=int(n)
copy_n=n
result = 0
i = len_n
while(n!=0):
    digit = n%10
    result=result+pow(digit,i)
    n=int(n/10)
    i = i - 1
if(result==copy_n):
    print("True")
else:
    print("False")