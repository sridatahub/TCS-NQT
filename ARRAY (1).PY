# # ----> repeated num conting/counting freq------->
# # n=int(input())
# # arr=list(map(int,input().split()))
# # freq={}
# # for i in arr:
# #     if i in freq:
# #         freq[i]+=1
# #     else:
# #         freq[i]=1
# # for key in freq:
# #     print(key, freq[key])            

# # remove duplictes from unsorted array
# # def remove_duplicates():
# #     n=int(input())
# #     arr=list(map(int,input().split())) 
# #     result=[]
# #     seen={}
# #     for i in arr:
# #         if i not in seen:
# #             result.append(i)
# #             seen[i]=1
# #     print(*result)        
# # remove_duplicates() 

# # left/right rotations of array
# # def array_rotation():
# #     n=int(input())
# #     arr=list(map(int,input().split()))
# #     k=int(input())
# #     direction=input()
# #     n=len(arr)
# #     k=k%n
# #     if direction=='L':
# #         result=arr[k:]+arr[:k]
# #     elif direction=='R':
# #         result=arr[-k:]+arr[:-k]
# #     print(*result) 
# # array_rotation()           

# # finding equilibrium in an array
# # def equilibrim():
# #      n=int(input())
# #      arr=list(map(int,input().split()))
# #      totalsum=sum(arr)
# #      leftsum=0
# #      for i in range(n):
# #           totalsum=totalsum-arr[i]
# #           if(total==leftsum):
# #                print(i)
# #                break
# #           leftsum=leftsm+arr[i]
# #      else:
# #           print(-1)
# # equilibrim()          

# # sort array according to another array
# # def sort():
# #     n1=int(input())
# #     arr1=list(map(int,input().split()))
# #     n2=int(input())
# #     arr2=list(map(int,input().split()))
# #     result=[]
# #     freq={}
# #     for i in arr1:
# #         if i in freq:
# #             freq[i]+=1
# #         else:
# #             freq[i]=1
# #     for i in arr2:
# #         if i in freq:
# #             result.extend([i]*freq[i])
# #             del freq[i]
# #     for x in sorted(freq):
# #         result.extend([x]*freq[x])
# #     print(*result)                 
# # sort()              
# # subset checking
# n1=int(input())
# arr1=list(map(int,input().split()))
# n2=int(input())
# arr2=list(map(int,input().split()))
# is_subset=True
# for i in arr2:
#     if i not in arr1:
#         is_subset=False
#         break
# if is_subset:
#     print("yes")
# else:
#     print("no")        
# (advanced array problems)
# max sum of any contiguuos sub array of size k
def sliding_window():
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,n):
        window_sum=window_sum+arr[i]-arr[i-k]
        if window_sum>max_sum:
            max_sum=window_sum
    print(max_sum)        
sliding_window()    