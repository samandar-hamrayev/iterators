class Divisors:
    def __init__(self, num):
        self.number = num

    def __iter__(self):
        self.curr = 1
        return self

    def __next__(self):
        if self.curr > self.number:
            raise StopIteration
        if self.number % self.curr == 0:
            result = self.curr
            self.curr += 1
            return result
        self.curr += 1
        return self.__next__() # rekursiv chaqiramiz va qayta natja olamiz



# berilgan sonning barcha butun bo'luvchilarini chop qilamiz
number = Divisors(120)
for div in number:
    print(div, end=", ")