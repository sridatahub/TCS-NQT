# selection sort
# n=int(input())
# arr=list(map(int,input().split()))
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if arr[min_index]>arr[j]:
#             min_index=j
#     arr[i],arr[min_index]=arr[min_index],arr[i]
# print(arr)           
# insertion sort
n=int(input())
arr=list(map(int,input().split()))
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)    
