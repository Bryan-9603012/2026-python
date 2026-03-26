from decimal import Decimal,localcontext
import math

print(round(1.27,1))
print(round(1.25361,3))
print(round(0.5))
print(round(2.5))

a = 1627731
print(round(a,-2))

print(4.2+2.1)
da,db = Decimal("4.2"),Decimal("2.1")
print(da+db)

with localcontext() as ctx:
    ctx.prec = 3
    print(Decimal("1.3")/Decimal("1.7"))
print(math.fsum([1.23e18,1,-1.23e18]))

x = 1234.56789
print(format(x,"0.2f"))
print(format(x,">10.1f"))
print(format(x,","))
print(format(x,"0.2f"))
print(format(x,"e"))

n = 1234
print(bin(n),oct(n),hex(n))
print(format(n,"b"),format(n,"x"))
print(int("4b2",16),int("2322",8))