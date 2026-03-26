import math 
import random
from fractions import Fraction

a = float("inf")
b = float("-inf")
c = float("nan")
print(a,b,c)
print(math.isinf(a))
print(math.isnan(c))
print(a+45,10/a)
print(a/a,a+b)
print(c==c)

p = Fraction(5,4)
q = Fraction(7,16)
r = q*p
print(p+q)
print(r.numerator,r.denominator)
print(float(r))
print(r.limit_denominator(8))
print(Fraction(*(3.75).as_integer_ratio()))

values = [1,2,3,4,5,6]
print(random.choice(values))
print(random.sample(values,3))
random.shuffle(values)
print(values)
print(random.random(0,10))
random.seed(42)
print(random.random())