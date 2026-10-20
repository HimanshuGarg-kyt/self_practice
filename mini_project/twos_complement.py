def to_binary(n):
    a = ""
    if n==0:
        return ""
    elif n%2 == 0:
        return to_binary(n//2) + "0"
    else:
        return to_binary(n//2) + "1"

def add1(b):
    if b[-1]=="0":
        return b[0:len(b)-1] + "1"
    else:
        return add1((b[0:len(b)-1])) + "0"
    
def twos_complement(n, bits):
    a = to_binary(n)
    if len(a) == bits-1:
        b = ""
        for i in a:
            if i == "0":
                b += i.replace("0","1")
            else:
                b += i.replace("1","0")

        c = add1(b)
        return "1" + c
    elif len(a) < bits-1:
        a = a.zfill(bits-1)
        b = ""
        for i in a:
            if i == "0":
                b += i.replace("0","1")
            else:
                b += i.replace("1","0")
        c = add1(b)
        return "1" + c
    else:
        return "cannot done operation, increase bits"

a = int(input("enter a number : "))
b = int(input("enter number of bits : "))
print(twos_complement(a,b))
