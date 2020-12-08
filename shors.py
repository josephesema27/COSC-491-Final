import math

class Shors:
    def __init__(self, num, divisor):
        self.num = num
        self.div = divisor
        self.true_prime = 3

    def isprime(self, number):
        if number % 2 == 0:
            return False
        for i in range(self.true_prime, number, 2):
            if number % i == 0:
                return False
        self.true_prime = number
        return True

    def gcd(self):
        factors = []
        if self.isprime(self.num):
            return self.num
        # #a = math.random.randint(2, self.num-1)
        # if self.div > self.num:
        #     self.num, self.div = self.div, self.num
        # while self.div > 0:
        #     self.num = self.num % self.div
        #     self.num, self.div = self.div, self.num
        for num in range(3, self.num, 2):
            if self.num % num == 0:
                if self.isprime(num):
                    factors.append(num)
        return factors

