class FibonacciSeq:
    def __init__(self, limit: int):
        try:
            limit = int(limit)
        except ValueError as err:
            # errorni print orqali qizartirib chiqarish
            print(f"Siz int tipida son kiritishingiz kerak: \033[31m{err}\33[0m")
        else:
            self.limit = limit

    def __iter__(self):
        self.fib1, self.fib2 = 0, 1 # boshlang'ich 2 ta qiymatni o'rnatib olamiz
        return self

    def __next__(self):
        if self.fib1 > self.limit: # limitdan oshgan bo'lsa iteratsiyani yakunlaymiz
            raise StopIteration
        val = self.fib1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2 # qiymatlarini yangilab olamiz
        return val


# 0 dann 100 gacha bo'lgan fibonacci ketma-ketliklarini chiqarish
fib = FibonacciSeq(100)
for i in fib:
    print(i, end=", ")

