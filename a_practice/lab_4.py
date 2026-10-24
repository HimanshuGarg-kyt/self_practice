# QUE 1
# def greetings(name):
#     return f"Hello, {name}!"

# a = input("enter a name : ")
# print(greetings(a))



# QUE 2
# def add(a,b):
#     return a + b

# a = float(input("ENTER FIRST NUMBER : "))
# b = float(input("ENTER SECOND NUMBER : "))
# print(add(a,b))



# QUE 3
# def calculate_age(name,birth_year):
#     return f"{name.title()} is {2026-birth_year} years old."

# a = input("ENTER YOUR NAME : ")
# b = int(input("ENTER YOUR BIRTH YEAR : "))
# print(calculate_age(a,b))



# QUE 4
# def fun(a):
#     if a%2 ==0:
#         return True
#     else:
#         return False

# a = int(input("ENTER NUMBER : "))
# print(fun(a))



# QUE 5
# def string_info(text):
#     return f"first character : {text[0]}\nlast character : {text[-1]}\nnumber of character : {len(text)}\nstring in upercase : {text.upper()}"

# a = input("ENTER YOUR TEXT : ")
# print(string_info(a))



# QUE 6
# def count_vowels(text):
#     count = 0
#     for i in text:
#         if i.lower() in "aeiou":
#             count += 1
#     return f"number of vowels is {count}"

# a = input("ENTER STRING : ")
# print(count_vowels(a))



# QUE 7
# def repeat_text(text, n):
#     print((text+ " ")*n ,sep = " ")

# a = input("enter text : ")
# b = int(input("enter number of times : "))
# repeat_text(a,b)



# QUE 8
# def larger(a,b):
#     return a if a>b else b

# print(larger(20,30))
# print(larger("him","garg"))



# QUE 9
# def clean_name(name) :
#     return name.strip().title()

# a = input("enter your name : ")
# print(clean_name(a))



# QUE 10
# def add1(a, b):
#     print(a + b)

# def add2(a, b):
#     return a + b

# x = add1(10, 20)
# print(x)

# y = add2(10, 20)
# print(y)



# QUE 11
# def power(base, exponent=2):
#     return base**exponent

# print(power(5,exponent = 5))



# QUE 12
# def  student_result(name, marks=0) :
#     if marks>=40:
#         return "Pass"
#     else:
#         return "Fail"

# print(student_result("gdc",50))



# QUE 13
# def format_student(name, roll, branch):
#     return f"{name} has roll no. {roll} and branch {branch}."

# print(format_student(name = "HIMANSHU",roll = "B26195",branch="CSE"))



# QUE 14
# def reverse_string(text):
#     a = ""
#     for i in range(-1,-(len(text)+1),-1):
#         a += text[i]
#     return a

# a = input("enter text : ")
# print(reverse_string(a))



# QUE 15
# def _palindrome(text):
#     b = ""
#     for i in text:
#         if i.isspace():
#             pass
#         else:
#             b += i.lower()
#     if b[::-1] == b:
#         return True
#     else:
#         return False

# a = input("ENTER TEXT : ")
# print(_palindrome(a))



# QUE 16
# def remove_vowels(text):
#     a = ""
#     for i in text:
#         if i.lower() in "aeiou":
#             pass
#         else:
#             a += i
#     return a

# a = input("ENTER TEXT : ")
# print(remove_vowels(a))



# QUE 17
# def calculator(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         if b == 0:
#             return "ZERO ERROR"
#         else:
#             return a / b
# a = int(input("ENTER a : "))
# b = int(input("ENTER b : "))
# c = input("ENTER OPERATION : ")
# print(calculator(a,b,c))



# QUE 18
# def test(): 
#     x = 20 
#     print("inside:", x) 
# x = 10 
# test() 
# print("outside:", x)



# QUE 19
# def test(): 
#     global x
#     x = 20 
#     print("inside:", x) 
# x = 10 
# print(x)
# test() 
# print("outside:", x)



# QUE 20
# def outer():
#     message = "Python"
#     def inner():
#         nonlocal message
#         print(message)
#         message = "Java"
#     inner()

# outer()



# QUE 22
# def my_sum(*args):
#     print(type(args))
#     return sum(args)

# print(my_sum(1,2,3,4,5))



# QUE 23
# def uppercase(a):
#     return a.upper()

# def reverse(a):
#     return a[::-1]

# def transform(text, operation):
#     if operation == "uppercase":
#         return uppercase(text)
#     elif operation == "reverse":
#         return reverse(text)

# a = input("ENETR TEXT : ")
# while True:
#     b = input("ENTER OPERATION(UPPERCASE,REVERSE) : ")
#     if b.lower() == "uppercase" or b.lower() == "reverse" :
#         print(transform(a,b.lower()))
#         break

#     else:
#         print("select appropriate operation")



# QUE 24
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = list(filter(lambda x:x%2==0,list1))
# list3 = list(map(lambda x:x**2,list2))
# print("original list : ",list1)
# print("filtered list : " ,list2)
# print("final list :" , list3)



# QUE 25
# names = ["Himanshu","Honey Singh","Ayush","Rajat"]
# marks = [19,15,12,9]

# def result(mark):
#     return "Pass" if mark >= 10 else "Fail"

# for i, (name, mark) in enumerate(zip(names, marks), start=1):

#     print(i, name, mark, result(mark))



# QUE 26
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# n = int(input("ENTER NUMBER : "))
# print(factorial(n))



# QUE 27
# def encrypt(text, shift):
#     a = ""
#     for i in text:
#         if i.isupper():
#             a += chr((ord(i)-ord("A")+shift)%26+ord("A"))
#         elif i.islower():
#             a += chr((ord(i)-ord("a")+shift)%26+ ord("a"))
#         else:
#             a += i
#     return a

# def decrypt(text, shift):
#     return encrypt(text, -shift)

# a = input("ENTER TEXT : ")
# print(encrypt(a,5))
# print(decrypt(encrypt(a, 5), 5) == a )



# QUE 28
# def word_report(para):
#     a = ""
#     for i in para:
#         if i.isspace() or i.isalnum():
#             if i.isalpha():
#                 a += i.lower()
#             else:
#                 a += i
#     a = a.split()
#     b = set(a)
#     return f"toatal number of words are {len(a)} and number of distinct words are {len(b)}, {a} , {b}"

# a = input("ENTER PARA : ")
# print(word_report(a))



# QUE 29
# PART 1
# def to_binary(n):
#     a = ""
#     if n==0:
#         return ""
#     elif n%2 == 0:
#         return to_binary(n//2) + "0"
#     else:
#         return to_binary(n//2) + "1"

# a = int(input("ENTER NUMBER : "))
# print(to_binary(a))

# PART 2
# def add1(b):
#     if b[-1]=="0":
#         return b[0:len(b)-1] + "1"
#     else:
#         return add1((b[0:len(b)-1])) + "0"
    
# def twos_complement(n, bits):
#     a = to_binary(n)
#     if len(a) == bits-1:
#         b = ""
#         for i in a:
#             if i == "0":
#                 b += i.replace("0","1")
#             else:
#                 b += i.replace("1","0")

#         c = add1(b)
#         return "1" + c
#     elif len(a) < bits-1:
#         a = a.zfill(bits-1)
#         b = ""
#         for i in a:
#             if i == "0":
#                 b += i.replace("0","1")
#             else:
#                 b += i.replace("1","0")
#         c = add1(b)
#         return "1" + c
#     else:
#         return "cannot done operation, increase bits"

# a = int(input("enter a number : "))
# b = int(input("enter number of bits : "))
# print(twos_complement(a,b))


# PART 3
# def find_unique(lst):
#     a = 0
#     for i in lst:
#         a = a^i
#     return a
# print(find_unique([4, 2,7, 7,  4]))



# QUE 30
# def to_binary(n):
#     a = ""
#     if n==0:
#         return ""
#     elif n%2 == 0:
#         return to_binary(n//2) + "0"
#     else:
#         return to_binary(n//2) + "1"

# def fraction(a):
#     b = ""
#     for i in range(23):
#         if a == 1.0:
#             b += "1"
#             return b + "0"*(22-i)
#         elif int((a%1) * 2) == 1 :   
#             b += "1"
#         else:
#             b += "0"
#         a *= 2
#     return b

# def ieee754(n):
#     a = ""
#     if n >= 0:
#         a += "0"
#     else:
#         a += "1"
#         n = -n
#     count = 0
#     while int(n) > 1:
#         n = n / 2
#         count += 1
#     a += to_binary(127+count).zfill(8)
#     a += fraction(n)
#     return a

# a = float(input("enter floating values : "))
# print(ieee754(a))