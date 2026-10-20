def to_binary(n):
    a = ""
    if n==0:
        return ""
    elif n%2 == 0:
        return to_binary(n//2) + "0"
    else:
        return to_binary(n//2) + "1"

def fraction(a):
    b = ""
    for i in range(23):
        if a == 1.0:
            b += "1"
            return b + "0"*(22-i)
        elif int((a%1) * 2) == 1 :   
            b += "1"
        else:
            b += "0"
        a *= 2
    return b

def ieee754(n):
    a = ""
    if n >= 0:
        a += "0"
    else:
        a += "1"
        n = -n
    count = 0
    while int(n) > 1:
        n = n / 2
        count += 1
    a += to_binary(127+count).zfill(8)
    a += fraction(n)
    return a

a = float(input("enter floating values : "))
print(ieee754(a))