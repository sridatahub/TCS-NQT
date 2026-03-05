def Sort_Array_According_to_Another_Array(arr1,arr2):
    result=[] 
    freq={} 
    for i in arr1:
        if i in freq:
            freq[i]+=1 
        else:
            freq[i]=1 
    for i in arr2: 
        if i in freq:
            result.extend([i]*freq[i]) 
            del freq[i]

    for x in sorted(freq):
        result.extend([x]*freq[x])

    print(*result)

n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
Sort_Array_According_to_Another_Array(arr1,arr2)
