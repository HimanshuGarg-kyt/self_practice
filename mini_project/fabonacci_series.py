# using recursion
def fibonacci(n):
    if n < 1:
        return "INVALID INPUT"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

    
n = int(input("enter number : "))
a = 0
b = 1
i = 0
while i<n:
    print(a)
    print(b)
    a += b
    b += a
    i+=2

