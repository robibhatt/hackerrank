#!/bin/python
prime = 1000000007
class Modulo:
    
    def __init__(self, p):
        self.p = p

    def product(self, numbers):
        sanitized = [x % self.p for x in numbers]
        answer = 1
        for s in sanitized:
            answer = (answer * s) % (self.p)
        return answer

    def sum(self, numbers):
        sanitized = [x % self.p for x in numbers]
        answer = 0
        for s in sanitized:
            answer = (answer + s) % (self.p)
        return answer

    def exponent(self, base, exponent):
        a = base % self.p
        b = exponent % (self.p - 1)
        if b == 0:
            return 1
        if a == 0:
            return 0
        if a == 1:
            return 1
        if b == 1:
            return (a % self.p)
        if b == 2:
            return ((a*a) % self.p)
        if b % 2 == 0:
            temp = self.exponent(a, b/2)
            return ((temp * temp) % self.p)
        else:
            temp = self.exponent(a, b/2)
            return ((temp * temp * a) % self.p)



# code snippet for illustrating input/output

num_tests = int(raw_input())
mod = Modulo(prime)
answers = []


for i in range(num_tests):

    N = int(raw_input())
    raw_b = raw_input()
    b = [int(x) for x in raw_b.split(' ')]
    stuff = []
    stuff.append(mod.exponent(mod.sum(b), N-2))
    for i in range(N):
        stuff.append(mod.exponent(b[i], b[i]-1))
    answers.append(mod.product(stuff))

for a in answers:
    print a



                   
