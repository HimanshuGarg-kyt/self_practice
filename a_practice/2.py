class Factory:
    a = "hello"

    def __init__(self,area,year,turnover):
        self.area = area
        self._year = year
        self.__turnover = turnover

    def hello(self):
        print(self.area)
        print(self._year)
        print(self.__turnover)

# class Factorypune(Factory):
#     def __init__(self,area,year,employee):
#         super().__init__(area,year)
#         self.employee = employee
    
s = Factory(530,2009,"100cr")
# s.hello()
# s.area = 1000
# s._year = 2009
# print(s.area)
# print(s._year)
# s.hello()

print(dir(Factory))
print(dir(s))