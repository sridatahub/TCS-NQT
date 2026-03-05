# pyramid pattern
# def pyramid_pattern():
#     n=int(input())
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print("  ",end="")
#         for k in range(i*2-1):
#             print("* ",end="")
#         print()
# pyramid_pattern()                

# diamond pattern
# def diamond_pattern():
#     n=int(input())
#     a=n-1
#     b=1
#     for i in range(1,n*2):
#         for j in range(a):
#             print("  ",end='')
#         for k in range(b):
#             print("* ",end="")
#         if i>=n:
#             a+=1 
#             b-=2
#         else:
#             a-=1
#             b+=2
#         print()
# diamond_pattern()                       

# line pattern(2n-1)(different code tried by me(owner))
def diamond_pattern():
    n=int(input())
    a=n-1
    b=1
    for i in range(1,n*2):
        for j in range(a):
            print("  ",end='')
        for k in range(b):
            print("* ",end="")
    if i>=n:
        a+=1 
        b-=2
    else:
        a-=1
        b+=2
    print()
diamond_pattern()                       

# chess pattern
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i+j)%2==0:
#             print("1",end="")
#         else:
#             print("0",end="") 
#     print()           

