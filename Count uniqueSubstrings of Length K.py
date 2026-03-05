s=input() 
k=int(input())
unique_substring=set() 
for i in range(len(s)-k+1):
    word=s[i:i+k]
    unique_substring.add(word) 
print(len(unique_substring))