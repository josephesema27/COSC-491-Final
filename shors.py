class Shors():
    def __init__(self, num, divisor):
        self.num = num
        self.div = divisor

    def gcd(self):
        if self.div > self.num:
            self.num, self.div = self.div, self.num
        while self.div > 0:
            self.num = self.num % self.div
            self.num, self.div = self.div, self.num
        return self.num

