n=int(input("Enter the Number:"))
#Prime Number Check
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        print(i)
        break
    if flag==1:
        print(n,"is not a Prime Number")
    else:
        print(n,"is a Prime Number")
#Palindrome
x=n
sum=0
while x>0:
    r=x%10
    sum=sum*10+r
    x=x//10
if sum==n:
    print(n,"is a Prime Palindrome")
else:
    print(n,"is not a Prime Palindrome")
