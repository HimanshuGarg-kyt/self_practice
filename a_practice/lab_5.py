# QUE 1
# def shout(text):
#     a = text.upper()
#     a+="!"
#     return a

# a = input("Enter a text : ")
# print(shout(a))

# QUE 2
# def initials(full_name):
#     if full_name == " " or full_name == "":
#         return ""
#     else:
#         a  =  full_name.split()
#         b = []
#         for i in a:
#             b.append(i[0].upper())
#         return ".".join(b) + "."

# a = input("enter : ")
# print(initials(a))

# QUE 3
# def mask_string(text, visible=4):
#     if visible <=0:
#         return "*"*len(text)
    
#     elif visible > len(text):
#         return text

#     else:
#         a = "*"*(len(text)-visible)
#         for i in range(len(text)-visible,len(text)):
#             a +=text[i]
#         return a 

# a = input("ENTER : ")
# print(mask_string(a))

# QUE 4
# def analyze_string(text):
#     return len(text),text.isalpha(),text.isdigit(),text.isalnum()

# a = input("Enter : ")
# print(analyze_string(a))

# QUE 5
#slicing que

# QUE 6
# def capitalize_words(sentence):
#     a = ""
#     for i in range(len(sentence)):
#         if sentence[i].isspace():
#             a+=" "
#         else :
#             if sentence[i-1].isspace() or i==0:
#                 a+=sentence[i].capitalize()
#             else:
#                 a += sentence[i]
#     return a

# a = input("Enter : ")
# print(capitalize_words(a))

# QUE 7
# def count_words_and_longest(para):
#     words = para.split()                     # split into tokens
#     word_count = len(words)                  # count words
#     longest_word = max(words, key=len)       # find longest by length
#     return (word_count, longest_word)

# a = input("Enter :  ")
# print(count_words_and_longest(a))

# QUE 9 
# def is_anagram(s1, s2):
#     for ch in s1:
#         if ch in s2:
#             s2 = s2.replace(ch,"",count = 1)
#         else:
#             return False
#     if s2 == "":
#         return True
#     else:
#         return False

# s1 = input("Enter : ")
# s2 = input("Enter : ")
# print(is_anagram(s1, s2))

# def is_anagram(s1, s2):
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     return sorted(s1) == sorted(s2)

# print(is_anagram("listen", "silent"))       # True
# print(is_anagram("Dormitory", "Dirty Room")) # True
# print(is_anagram("hello", "world"))         # False

# QUE 12
# def pig_latin(word, suffix="ay"):
#     return word[1:] + word[0] + suffix

# a = input("Enter : ")
# print(pig_latin(a))

# QUE 13 
# def tag(text, prefix="[", suffix="]"):  
#     return prefix + text + suffix  
# a = "python"
# print(tag(a))
# print(tag(a,"<",">"))
# print(tag(a,suffix = "!"))
# print(tag("data","{","}"))

# QUE 14
# names = ["Amit", "Ramesh", "Raj", "Priyanka", "Om"]
# check = lambda name : name.upper() 
# a = list(map(check , names))
# check1 = lambda x:len(x)>4
# b = list(filter(check1,names))
# print(names)
# print(a)
# print(b)

# QUE 15
# def remove_duplicates_preserve_order(text):
#     list1 = []0000
#     for ch in text:
#         if ch not in list1:
#             list1.append(ch)
#     return "".join(list1)

# a = input("Enter  :  ")
# print(remove_duplicates_preserve_order(a))