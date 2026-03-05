n=int(input())
arr=list(map(int,input().split()))
m=int(input())
#{180, 180, 200, 200, 200, 200, 200, 200, 220}
#4  800 
count=1 
for i in range(n):
    if arr[i]==arr[i+1]:
        count+=1 
        if count==m:
            print(arr[i]*m)
            break 
    else:
        count=1 
    

