class Demo:
    def __setattr__(self, key, value):
        print(key, value)
        self.__dict__[key] = value

d = Demo()

d.name = "Himanshu"