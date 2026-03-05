str1=input() 
str2=input() 
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    freq={} 
    for ch in str1:
        if ch in freq:
            freq[ch]+=1 
        else:
            freq[ch]=1 
    for ch in str2:
        if ch in freq:
            freq[ch]-=1 
        else:
            print("Not Anagram")
            break
    else:
        for ch in freq:
            if freq[ch]!=0:
                print("Not Anagaram")
                break 
        print("Anagarm")