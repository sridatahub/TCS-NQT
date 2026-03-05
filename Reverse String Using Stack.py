s=input() 
stack=[]
for ch in s:
    stack.append(ch)
result="" 
while stack: 
    result+=stack.pop()
print(result)




