def Array_Rotation(arr,k,direction):
    n=len(arr) 
    
    k=k%n 
    if direction=='L':
        result=arr[k:]+arr[:k]
    elif direction=='R':
        result=arr[-k:]+arr[:-k]
    print(*result)
    
n=int(input()) 
arr=list(map(int,input().split()))
k=int(input())
direction=input() 
Array_Rotation(arr,k,direction)