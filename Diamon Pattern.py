def diamond_pattern(n):
    a=n-1
    b=1
    for i in range(1,n*2):
        for j in range(a):
            print("  ",end="")
        for k in range(b):
            print("* ",end="")
        if i>=n:
            a+=1
            b-=2
        else:
            a-=1
            b+=2
        print()
n=int(input())
diamond_pattern(n)