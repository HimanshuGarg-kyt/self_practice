import copy
# QUE 1
# class Student:
#     pass

# Ram = Student()
# Sam = Student()
# print(Ram) #object class name and its memory location
# print(Sam) #object class name and its memory location
# print(dir(Student()))
# Student.name = "Harsh Sharma"
# Student.department = "Data Science"
# Sam.department = "Computer Science"

# print(Ram.name , Ram.department) 
# print(Sam.name , Sam.department)

# print(dir(Sam))



# QUE 2
# class Bike:
#     def __init__(self):
#         pass

#     def accelarate(self):
#         print("Used for acceleration")

#     def brake(self):
#         print("Used to stop break")

# bike1 = Bike()
# bike2 = Bike()
# bike1.brake()



# QUE 3
# class Car: 
#     manufacturer = 'Maruti' 
 
#     def __init__(self, name, year): 
#         self.name = name 
#         self.year = year 
 
# t = Car('Wagon R', 2019) 
# r = Car('Alto', 2010) 
 
# print(r.manufacturer, t.manufacturer) 
# t.manufacturer = 'Honda' 
# t.name = 'City' 
# print(t.manufacturer, t.name, t.year) 
# print(r.manufacturer, Car.manufacturer) 
 
# Car.manufacturer = 'Suzuki' 
# print(t.manufacturer, r.manufacturer) 



# QUE 4
# class Student:
#     college = 'IIT Mandi'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def add_details(self):
#         self.departmant = "Computer Science"


# c1 = Student("Himanshu", 18)

# c2 = Student("Bhavik", 18)

# c2.college = "MMDU"

# c1.add_details()
# c2.add_details()

# print(c1.name, c1.age, c1.college, c1.departmant)
# print(c2.name, c2.age, c2.college, c2.departmant)



# # QUE 5
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)

#     def is_square(self):
#         return self.length == self.breadth


# a = int(input("ENTER LENGTH : "))
# b = int(input("ENTER BREADTH : "))
# s = Rectangle(a, b)
# print(s.area(), s.perimeter(), s.is_square())



# QUE 6
# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b

#     def subtarct(self):
#         return self.a - self.b

#     def multiply(self):
#         return self.a * self.b

#     def divide(self):
#         if self.b != 0:
#             return self.a / self.b
#         else:
#             return "Cannot divide by zero"


# a = Math(10, 0)
# print(f"{a.add()}, {a.subtarct()}, {a.multiply()}, {a.divide()}")



# QUE 7
# class Statistics:
#     def __init__(self,a):
#         self.a = a

#     def mean(self):
#         sum = 0
#         for i in self.a:
#             sum += i
#         return f"mean of the numbers is {sum/len(self.a)}"

#     def median(self):
#         temp = self.sorted_list()
#         if len(temp) % 2 == 0:
#             a = (temp[int(len(temp)/2)] + temp[int((len(temp)/2)-1)])/2
#             return f"median of the numbers is {a}"
#         else:
#             a = temp[int(((len(temp)+1)/2)-1)]
#             return f"median of the numbers is {a}"

#     def stDeviation(self):
#         sum = 0
#         for i in self.a:
#             sum += i    
#         mean = sum / len(self.a)   
#         sum = 0
#         for i in self.a:
#             sum += (i - mean)**2
#         st = (sum/len(self.a))**(1/2)
#         return f"standard deviation of the numbers is {st}"

#     def maximum(self):
#         m = None
#         for i in self.a:
#             if m == None or m < i:
#                 m = i
#         return f"maximum of the numbers is {m}"

#     def minimum(self):
#         m = None
#         for i in self.a:
#             if m == None or m > i:
#                 m = i
#         return f"minimum of the numbers is {m}"

#     def mode(self):
#         t = self.sorted_list()
#         best_count, best_value, count = 0, None, 0
#         for i in range(len(t)):
#             if i > 0 and t[i] == t[i - 1]:
#                 count += 1
#             else:
#                 count = 1
#             if count > best_count:
#                 best_count, best_value = count, t[i]
#         return f"mode of numbers is {best_count, best_value}"

#     def sorted_list(self):
#         a = len(self.a)
#         b = copy.deepcopy( self.a)
#         for i in range(a):
#             for j in range(a-i-1):
#                 if b[j] > b[j+1]:
#                     b[j] , b[j+1] = b[j+1] , b[j]
#         return b

#     def show(self):
#         print(self.median())
#         print(self.mode())
#         print(self.mean())
#         print(self.maximum())
#         print(self.minimum())
#         print(self.sorted_list())
#         print(self.a)
#         print(self.stDeviation())   

# a = Statistics([10, 5, 2, 11, 7, 2, 2, 3, 5])

# a.show()



# QUE 8

# QUE 9
# QUE 10
# QUE 11
# QUE 12