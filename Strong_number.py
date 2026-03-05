n=int(input())
sum=0 
temp=n 
while n>0: 
    rem=n%10 
    fact=1 
    for i in range(1,rem+1):
        fact=fact*i 
    sum+=fact 
    n=n//10 
if temp==sum:
    print("Strong number")
else:
    print("Not Strong number")

