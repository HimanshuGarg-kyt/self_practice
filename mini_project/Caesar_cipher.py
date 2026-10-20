def encrypt(text, shift):
    a = ""
    for i in text:
        if i.isupper():
            a += chr((ord(i)-ord("A")+shift)%26+ord("A"))
        elif i.islower():
            a += chr((ord(i)-ord("a")+shift)%26+ ord("a"))
        else:
            a += i
    return a

def decrypt(text, shift):
    return encrypt(text, -shift)

a = input("ENTER TEXT : ")
print(encrypt(a,5))
print(decrypt(encrypt(a, 5), 5) == a )