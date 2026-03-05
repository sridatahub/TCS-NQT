s=input() 
words=list(s) 
n=len(words)
for i in range(n):
    for j in range(i+1,n):
        if words[i]>words[j]:
            words[i],words[j]=words[j],words[i] 
result="".join(words)
print(result)