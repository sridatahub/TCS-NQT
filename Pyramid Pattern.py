def pyramid_pattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print("  ",end="")
        for k in range(i*2-1):
            print("* ",end="")
        print()

        
n=int(input())
pyramid_pattern(n)