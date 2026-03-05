s=input() 
words=s.split() 
max_repeat=0 
result_word=""
for word in words:
    freq={} 
    for ch in word:
        if ch in freq:
            freq[ch]+=1 
        else:
            freq[ch]=1
    current_max=max(freq.values()) 
    if current_max>max_repeat:
        max_repeat=current_max 
        result_word=word 
print(result_word)