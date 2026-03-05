# checking strong num or not strong num means--->ex 145 dividing into 3 1,4,5 finding their factorial values and by adding them if we get same num after adding then it is called strong num
# n=int(input())
# sum=0 
# temp=n
# while n>0:
#     rem=n%10
#     fact=1
#     for i in range(1,rem+1):
#         fact=fact*i
#     sum+=fact
#     n=n//10
# if temp==sum:
#     print("strong number")
# else:
#     print("not strong number")            

# checking perfect number/not--->ex: 6 divisibles of 6 are 1,2,3 if we get the same num by adding the divisibles of that num then it is a perfect num and 1 never be a perfect num
# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("perfect number")
# else:
#     print("not perfect number")            
# AMstrong num
# n=int(input())
# digit=len(str(n))
# sum=0
# temp=n
# while n>0:
#     rem=n%10
#     sum+=rem**digit
#     n//=10
# if temp==sum:
#     print("AMSTRONG NUMBER")
# else:
#     print("NOT AMSTRONG NUMBER")     

# greatest common divisor
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# while b!=0:
#     a,b=b,a%b
# print(a)  

# least common multiplier
a=int(input("enter a:"))
b=int(input("enter b:"))
x=a
y=b
while b!=0:
    a,b=b,a%b
gcd=a    
lcm=(x*y)//gcd
print(gcd)
print(lcm)
