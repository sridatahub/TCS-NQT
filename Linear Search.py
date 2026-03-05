n=int(input())
arr=list(map(int,input().split()))
k=int(input())
found=False 
for i in range(n):
    if arr[i]==k:
        found=True 
        print(i)
        break
if not found:
    print("Not Found")
        
