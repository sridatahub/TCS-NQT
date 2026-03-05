s=input() 
result="" 
#heLLo12
for letter in s:
    if letter.islower():
        result+=letter.upper() 
    elif letter.isupper():
        result+=letter.lower() 
    else:
        result+=letter 
print(result)