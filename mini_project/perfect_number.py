#CHECK FOR A PERFECT NUMBER

import sys

sys.setrecursionlimit(10000)

def perfect_number1(n,a=2):
    if a > n:
        return 0
    elif n%a==0: 
        return perfect_number1(n,a+1) + n//a
    else:
        return perfect_number1(n,a+1)

def perfect_number(a):
    if a == perfect_number1(a):
        return f"{a} IS PERFECT NUMBER"
    else:
        return f"{a} IS NOT PERFECT NUMBER"

a = int(input("ENTER A NUMBER : "))
print(perfect_number(a))  # examples of perfect numbers are 6, 28, 496, 8128

