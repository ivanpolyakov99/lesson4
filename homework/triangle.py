import math

def sqt(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            p =(a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))
