# recursion---->function calling itself
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# n=int(input())
# print(factorial(n))

# fibonacci series
def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n))    