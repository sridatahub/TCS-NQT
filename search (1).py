# linear search time complexity-o(n) more time than binary search
# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# found=False
# for i in range(n):
#     if arr[i]==k:
#         found=True 
#         break
# if found:
#     print("found")
#     print(i)      -------> add to find index value
# else:
#     print("not found")        

# binary search time complexity--->o(logn) less time taken than linear search
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
k=int(input())
left=0
right=n-1
found=False
while left <= right:
    mid=(left+right)//2
    if arr[mid]==k:
        found=True
        print("found")
        print(mid)
        break
    elif k>arr[mid]:
        left=mid+1
    else: 
        right=mid-1
if not  found:
    print("not found")                 


    