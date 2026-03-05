n=int(input()) 
arr=list(map(int,input().split()))
count=0 
max_count=0 
#{1, 1, 0, 1, 1, 1}. 
for i in range(n):
    if arr[i]==1:
        count+=1 
        if count>max_count:
            max_count=count
    else:
        count=0  
print(max_count)
