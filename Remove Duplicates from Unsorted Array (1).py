def Remove_Duplicates_from_Unsorted_Array(n,arr):
    result=[] 
    seen={} 
    for i in arr:
        if i not in seen:
            result.append(i)
            seen[i]=1 
    print(*result)
n=int(input())
arr=list(map(int,input().split()))
Remove_Duplicates_from_Unsorted_Array(n,arr)