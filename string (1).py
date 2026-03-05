# frequency of char in string
# word=input()
# freq={}
# for ch in word:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq) 
 
# first non repeating char in string
# word=input()
# freq={}
# for ch in word:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# found=False
# for ch in freq:
#     if freq[ch]==1:
#         print(ch)
#         found=True
#         break
# if not found:
#     print(-1)
    
# ANAGRAM---> IF WORDS AND LEN ARE EQUAL ORDER DOEN'T MATTER 
# str1="anagram"
# str2="nagaram "        
# str1 and 2 are anagram
# str1=input("enter str1:")
# str2=input("enter str2:")
# if len(str1)!=len(str2):
#     print("Not Anagram")
# else:
#     freq={}
#     for ch in str1:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1
#     for ch in str2:
#         if ch in freq:
#             freq[ch]-=1
#         else:
#             print("Not Anagram")
#             break
#     else:
#         for ch in freq:
#             if freq[ch]!=0:
#                 print("not anagram")
#                 break
#         print("anagram")

#reverse words in strings
# word=input()
# words=word.split()
# words.reverse()
# result=" ".join(words)
# print(result) 

# 10. remove letters from first string present in the second string
# str1=input()
# str2=input()
# result=''
# for ch in str1:
#     if ch not in str2:
#         result+=ch
# print(result)

# largest word in a string
# s=input("enter string:")
# words=s.split()
# max_len=0
# max_words=""
# for word in words:
#     if len(word)>max_len:
#         max_len=len(word)
#         max_word=word
# print(max_word)

# change the case of each char in str(upper-lower and viceversa) 
# ex heLLO-->HEllo num remains same
# s=input()
# result="" 
# for letter in s:
#     if letter.islower():
#         result+=letter.upper()
#     elif letter.isupper():
#         result+=letter.lower()
#     else:
#         result+=letter
# print(result)                

# bubble sort in str
# s=input()
# words=list(s)
# n=len(words)
# for i in range(n):
#     for j in range(i+1,n):
#         if words[i]>words[j]:
#             words[i],words[j]=words[j],words[i]
# result="".join(words)
# print(result)

# finding word in a given string which has highest no.of repeated lettera
# s=input()
# words=s.split()
# max_repeat=0
# result_word=" " 
# for word in words:
#     freq={}
#     for ch in word:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1
#     current_max=max(freq.values())
#     if current_max>max_repeat:
#         max_repeat=current_max
#         result_word=word
# print(result_word)                    

# substring or not
# s=input()
# sub=input()
# flag=False
# for i in range(len(s)-len(sub)+1):
#     if s[i:i+len(sub)]==sub:
#         flag=True
#         print(i)
#         break
# if not flag:
#     print("-1")   

# change every letter with the next lexico graphics alphabet in the given str
# word=input()
# result=""
# for ch in word:
#     if ch=='Z':
#         result+='A'
#     elif ch=='z':
#         result+='a'  
#     elif ch.islower():
#         result+=chr(ord(ch)+1)
#     elif ch.isupper():
#         result+=chr(ord(ch)+1) 
#     else:
#         result+=ch
# print(result)        

