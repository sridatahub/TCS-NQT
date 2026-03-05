n=int(input())
digit=len(str(n))
sum=0
temp=n 
while n>0:
    rem=n%10 
    sum+=rem**digit 
    n//=10
if temp==sum:
    print("Amstrong Number")
else:
    print("Not Amstrong Number") 
