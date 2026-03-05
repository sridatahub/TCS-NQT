s=input()
stack=[]
pairs={')':'(','}':'{',']':'['}
for ch in s:
    #Open 
    if ch in pairs.values():
        stack.append(ch)
    #close 
    elif ch in pairs:
        if not stack or stack[-1]!=pairs[ch]:
            print("Not Valid")
            break
        stack.pop()
else:
    if not stack:
        print("Valid")
    else:
        print("Not Valid")
        
    


    
    

