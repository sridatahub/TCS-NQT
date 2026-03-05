n=int(input())
arr=list(map(int,input().split()))
arr.sort()
k=int(input())
left=0
right=n-1 
found=False
while left<=right:
    mid=(left+right)//2 
    if arr[mid]==k:
        found=True 
        print(mid)
        break 
    elif k>arr[mid]:
        left=mid+1 
    elif k<arr[mid]:
        right=mid-1 
if not found:
    print("Not Found")
