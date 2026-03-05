word=input() 
freq={} 
for ch in word:
    if ch in freq:
        freq[ch]+=1 
    else:
        freq[ch]=1 
found=False 
for ch in freq:
    if freq[ch]==1:
        print(ch)
        found=True 
        break 
if not found:
    print("-1")