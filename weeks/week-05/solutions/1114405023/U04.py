import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

print(round(0.5)) 
print(round(2.5)) 
print(round(3.5)) 

def trad_round(x: float, n: int = 0) -> Decimal:
    d = Decimal(str(x))
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  
print(trad_round(2.5))  

c = float("nan")
print(c == c) 
print(c == float("nan")) 
print(math.isnan(c))

data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  

print(0.1 + 0.2 == 0.3)

print(Decimal("0.1") + Decimal("0.2")) 
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3")) 

t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
