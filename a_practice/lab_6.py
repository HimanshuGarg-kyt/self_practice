# QUE 1
# def factorial(num):
#     if num == 0:
#         return 1
    
#     elif num <0:
#         return "NOT DEFINED"
    
#     else:
#         return num * factorial(num - 1)

# a = int(input("ENTER A NUMBER : "))
# print("Factorial using recursion:", factorial(a))

# b = 1
# if a == 0:
#     b = 1
# else:
#     for i in range(1, a + 1):
#         b *= i
# print("Factorial without recursion:", b)



# QUE 2
# def fibonacci(n):
#     if n < 1:
#         return "INVALID INPUT"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# a = int(input("ENTER A NUMBER : "))
# print(fibonacci(a))

# x, y = 0, 1
# list1 = []

# if a < 1:
#     print("invalid input")
# elif a == 1:
#     list1.append(str(0))
# elif a == 2:
#     list1.append(str(0))
#     list1.append(str(1))
# else:
#     list1.append(str(0))
#     list1.append(str(1))
#     for i in range(a - 2):
#         c = x + y
#         list1.append(str(c))
#         x, y = y, c
#     print(c)

# print(", ".join(list1))



# QUE 3
# def to_binary(n):
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:
#         return to_binary(n // 2) + str(n % 2)

# a = int(input("Enter a number: "))
# print(to_binary(a))



# QUE 4
# def p(s):
#     if len(s) == 1:
#         return True

#     elif len(s) == 0:
#             return True
    
#     elif s[0]==s[len(s)-1]:
#         return p(s[1:len(s)-1])

#     else:
#         return False

# a = input("ENETR A STRING : ")
# b = p(a)
# if b:
#     print(f"{a} is palindrome")
# else:
#     print(f"{a} is not palindrome")



# QUE 5
# def sum_digit(n):
#     if n == 0:
#         return 0 

#     elif n<0:
#         return "ERROR"

#     else:
#         return sum_digit(n//10) + n%10

# a = int(input("ENETR A NUMBER : "))
# print(sum_digit(a))



# QUE 6
# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n - 1)

# print(power(5, 3))



# QUE 7
# def sum_list(a):
#     if a == []:
#         return 0
#     else:
#         return int(a[0]) + sum_list(a[1:])

# a = input("Enter numbers separated by space: ")
# b = a.split()
# print(sum_list(b))



# QUE 8
# def reverse_string(s):
#     if len(s) == 1:
#         return s[0]
#     else:
#         return s[-1] + reverse_string(s[:-1])

# print(reverse_string("Recursion"))



# QUE 9
# def find_max(n):
#     if len(n)==1:
#         return n[0]

#     elif int(n[0])>int(n[1]):
#         n.pop(1)
#         return find_max(n)

#     else:
#         return find_max(n[1:])

# a = input("Enter numbers separated by space: ")
# b = a.split()
# print(find_max(b))



# QUE 10
# def count_vowel(s):
#     a = "aeiouAEIOU"
#     if len(s) == 0:
#         return 0

#     else:
#         if s[0] in a:
#             return count_vowel(s[1:]) + 1
#         else :
#             count_vowel(s[1:])

# a = input("ENTER A STRING : ")
# print(count_vowel(a))



# QUE 11
# def diagonal_sum(mat, i=0):
#     if i==len(mat):
#         return 0

#     return mat[i][i] + diagonal_sum(mat,i=i+1)

# n = int(input("enter  :  "))
# matrix = []
# for k in range(n):
#     row = []
#     for value in input().split():
#         row.append(int(value))
#     matrix.append(row)

# print("sum", diagonal_sum(matrix))
# print(matrix)

# QUE 12
# def count_element(mat, target, r=0, c=0):
#     if r == len(mat):                          # Base case: all rows are done
#         return 0
#     if c == len(mat[0]):                          # End of a row: go to the next row
#         return count_element(mat, target, r+1 , 0)
#     if mat[r][c] == target:
#         return 1 + count_element(mat, target, r, c + 1)
#     return count_element(mat, target, r, c+1)
# rows = int(input("Enter the number of rows: "))
# matrix = []
# for k in range(rows):
#     row = []
#     for value in input().split():
#         row.append(int(value))
#     matrix.append(row)
# target = int(input("Enter the number to count: "))
# print(target, "appears", count_element(matrix, target), "time(s)")