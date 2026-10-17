a = int(input("enter first number : "))
b = int(input("enter second number : "))
list = []
# if a==0 or b==0:
#     print(a if a!= 0 else b)

# else:
#     for i in range(1,a+1):
#       if a%i==0:
#           list.append(i)

#     for el in list:
#       if b%el==0:
#           c=el
#     print(c)

def hcf(first,second):
    if second==0:
      print(first)
    else:
      return hcf(second,first%second)

hcf(a,b)
# print(5%2)