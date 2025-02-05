class GeomerticProgression:
    def __init__(
            self,
            start: int | float,
            ratio: int | float,
            limit: int
    ):
        assert start != 0, "Geometrik progressiya hadi 0 bo'lishi mantiqsiz."
        assert ratio != 0, "Geometrik progressiya maxraji 0 bo'lishi mumkin emas."
        assert limit >= 1, "Limit 1 dan kam bo'la olmaydi, u necha had chiqishini belgilaydi."

        self.start = start
        self.ratio = ratio
        self.limit  = limit

    def __iter__(self):
        self.count = 0 # limitga ketganda to'xtatish uchun
        self.current = self.start
        return  self

    def __next__(self):
        if self.count > self.limit:
            raise StopIteration
        val = self.current
        self.current *= self.ratio
        self.count += 1
        return  round(val, 4) # velguldan keyin 4 aniqlikda chiqarish


# 2 dan keyingi 10 hadni chop etish, 1.2 ko'paytma qadam bilan
obj = GeomerticProgression(2, 0.4, 10)
for i in obj:
    print(i)



