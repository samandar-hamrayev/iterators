class OddNumbers:
    # toq sonlarni chiqarish uchun start va end
    # limitlarni berish kerak, agarda bitta
    # arg kelsa uni avtomatik end ga olamiz
    def __init__(
            self,
            start: int | None = None,
            end: int | None = None
    ):
        if start is None and end is None:
            raise TypeError("Kamida bitta arg berilishi kerak.")

        self.start = start if end is not None else 1 # agar endga qiymat kelmasa berilgan qiymat end uchun
        self.end = end if end is not None else start

    def __iter__(self):
        self.step = 2 if self.start <= self.end else -2
        self.current = self.start
        if self.start % 2 == 0: # start limit toqligi va stepning -2 yoki 2 ligiga qarab currenni sozlab olamiz
            if self.step == 2:
                self.current = self.start + 1
            else:
                self.current = self.start - 1
        return self

    def __next__(self):
        if self.step == 2 and self.current > self.end: # end dan katta bo'lganda iteratsiya yakunlanadi
            raise  StopIteration
        if self.step == -2 and self.current < self.end:
            raise StopIteration
        res = self.current
        self.current += self.step
        return res

def print_nums(obj: OddNumbers) -> None: # odd larni print qilish uchun
    for odd in obj:
        print(odd, end=', ')



# start'dan end katta holat uchun
print("startdan end katta holatda:")
odds = OddNumbers(2, 15)
print_nums(odds)


# start'dan end kichik holat uchun
print("\nstartdan end kichik holatda:")
odds = OddNumbers(11, 4)
print_nums(odds)

# bitta arg kelgan holatda yani bunda bittasi end ga olinadi start ga 0 olinadi
print("\nbitta argument: musbat berilgan holatda:")
odds = OddNumbers(20)
print_nums(odds)


# bitta arg kelgan holatda yani bunda bittasi end ga olinadi start ga 0 olinadi
# bunda 0 dan boshlab o'sha songacha manfity toq sonlarini berish kerak
print("\nbitta argument: manfiy berilgan holatda:") #
odds = OddNumbers(-19)
print_nums(odds)