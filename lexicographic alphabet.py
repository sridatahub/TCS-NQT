word=input()
result="" 
for ch in word:
    if ch=='Z':
        result+='A'
    elif ch=='z':
        result+='a'
    elif ch.islower():
        result+=chr(ord(ch)+1)
    elif ch.isupper():
        result+=chr(ord(ch)+1)
    else:
        result+=ch
print(result)