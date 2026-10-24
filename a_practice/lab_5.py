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
#         b = ""
#         for i in a:
#            b += i[0].upper() + "."
#         return b

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



# QUE 8
# def format_report_card(name, marks, grade):
#     print(f"Name: {name:<10} | Marks: {marks:.3f} | Grade: {grade}") 

# format_report_card("Himanshu",95,"A+")
# format_report_card("Bhavik",90,"A")



# QUE 9 
# def is_anagram(s1, s2):
#     s1 = s1.replace(" ","")
#     a = s2.lower().replace(" ","")
#     for ch in s1:
#         if ch.lower() in a:
#             a = a.replace(ch.lower(),"",count = 1)
#         else:
#             return False
#     if a == "":
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



# QUE 10
# def is_valid_password(password):
#     lower = any(el.islower() for el in password)
#     upper = any(el.isupper() for el in password)
#     digit = any(el.isdigit() for el in password)
#     requirment = [len(password)>=8, upper, lower, digit ]
#     return all(requirment)

# a = input("ENTER PASSWORD : ")
# print(is_valid_password(a))



# QUE 11
# def count_char_recursive(text, ch):
#     if len(text) == 0:
#         return 0
#     elif text[0] == ch:
#         return count_char_recursive(text[1:],ch) + 1
#     else:
#         return count_char_recursive(text[1:],ch)

# a = input("ENTER TEXT : ")
# b = input("ENTER COUNTING CHARACTER : ")
# print(count_char_recursive(a,b))



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
#     list1 = []
#     for ch in text:
#         if ch not in list1:
#             list1.append(ch)
#     return "".join(list1)

# a = input("Enter  :  ")
# print(remove_duplicates_preserve_order(a))



# BROWNIE QUESTION 
# B1
# def run_length_encode(text):
#     # a = None
#     # b = []
#     # c = ""
#     # i = 0
#     # while i <len(text):
#     #     if text[i] == a:
#     #         i += 1
#     #         pass
#     #     else:
#     #         a = i
#     #         c += i + str(text.count(i))
#     #         i += 1
#     # return c
#     if text == "":
#         return ""

#     result = ""
#     count = 1

#     for i in range(1, len(text)):

#         if text[i] == text[i - 1]:
#             count += 1
#         else:
#             result += text[i - 1] + str(count)
#             count = 1

#     result += text[-1] + str(count)

#     return result

# def run_length_decode(code):
#     i = 0
#     a = ""
#     while i < len(code):
#         ch = code[i]
#         i += 1
#         num = ""
#         while i < len(code) and code[i].isdigit():
#             num += code[i]
#             i += 1
#         a += ch * int(num)
#     return a

# text = input("ENTER STRING : ")
# print(run_length_encode(text))
# # print(run_length_decode(text))
# print(run_length_decode(run_length_encode(text)) == text)