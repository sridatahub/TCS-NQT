def Equilibrium(n,arr):
    totalsum=sum(arr) 
    leftsum=0 
    for i in range(n):
        totalsum=totalsum-arr[i] 
        if(totalsum==leftsum):
            print(i)
            break
        leftsum=leftsum+arr[i] 
    else:
        print(-1)

n=int(input())
arr=list(map(int,input().split()))
Equilibrium(n,arr)
