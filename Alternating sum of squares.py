n=int(input())
arr=list(map(int,input().split()))
total=0 
for i in range(n):
    square=arr[i]*arr[i] 
    if i%2==0:
        total+=square 
    else:
        total-=square 
print(total)