import copy
class Statistics:
    def __init__(self,a):
        self.a = a

    def mean(self):
        sum = 0
        for i in self.a:
            sum += i
        return f"mean of the numbers is {sum/len(self.a)}"

    def median(self):
        temp = self.sorted_list()
        if len(temp) % 2 == 0:
            a = (temp[int(len(temp)/2)] + temp[int((len(temp)/2)-1)])/2
            return f"median of the numbers is {a}"
        else:
            a = temp[int(((len(temp)+1)/2)-1)]
            return f"median of the numbers is {a}"

    def stDeviation(self):
        sum = 0
        for i in self.a:
            sum += i    
        mean = sum / len(self.a)   
        sum = 0
        for i in self.a:
            sum += (i - mean)**2
        st = (sum/len(self.a))**(1/2)
        return f"standard deviation of the numbers is {st}"

    def maximum(self):
        m = None
        for i in self.a:
            if m == None or m < i:
                m = i
        return f"maximum of the numbers is {m}"

    def minimum(self):
        m = None
        for i in self.a:
            if m == None or m > i:
                m = i
        return f"minimum of the numbers is {m}"

    def mode(self):
        t = self.sorted_list()
        best_count, best_value, count = 0, None, 0
        for i in range(len(t)):
            if i > 0 and t[i] == t[i - 1]:
                count += 1
            else:
                count = 1
            if count > best_count:
                best_count, best_value = count, t[i]
        return f"mode of numbers is {best_count, best_value}"

    def sorted_list(self):
        a = len(self.a)
        b = copy.deepcopy( self.a)
        for i in range(a):
            for j in range(a-i-1):
                if b[j] > b[j+1]:
                    b[j] , b[j+1] = b[j+1] , b[j]
        return b

    def show(self):
        print(self.median())
        print(self.mode())
        print(self.mean())
        print(self.maximum())
        print(self.minimum())
        print(self.sorted_list())
        print(self.a)
        print(self.stDeviation())   

a = Statistics([5, 6, 8, 125])

a.show()