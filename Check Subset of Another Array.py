n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
is_subset=True 
for i in arr2:
    if i not in arr1:
        is_subset=False 
        break
if is_subset:
    print("Yes")
else: 
    print("No")