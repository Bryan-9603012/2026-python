class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @classmethod
    def from_string(cls, s):
        """從 '3,4' 這種字串建立 Point"""

        x, y = map(int, s.split(','))
        return cls(x, y)

    @classmethod
    def from_list(cls, lst):
        """從 [3, 4] 這種 list 建立 Point"""
        return cls(lst[0], lst[1])

    @classmethod
    def origin(cls):
        """原點的工廠方法"""
        return cls(0, 0)

print("=== @classmethod 多重構造器 ===")
p1 = Point(3, 4)
p2 = Point.from_string("3,4")
p3 = Point.from_list([3, 4])
p4 = Point.origin()
print(p1, p2, p3, p4)


class ColoredPoint(Point):
    def __init__(self, x, y, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, color={self.color!r})"

print("\n=== 繼承時 cls 指向子類 ===")
cp = ColoredPoint.from_string("5,6")
print(cp)
print(type(cp))


class CostTable:
    """儲存 36 個字元（0-9, A-Z）各自的印刷成本"""

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, costs):
        self.costs = costs

    def cost_of(self, digit_index):
        return self.costs[digit_index]

    def total_cost(self, n, base):
        """計算數字 n 在 base 進位下的總印刷成本"""
        if n == 0:
            return self.costs[0]
        total = 0
        while n > 0:
            total += self.costs[n % base]
            n //= base
        return total

    @classmethod
    def uniform(cls, cost=1):
        """建立所有字元成本相同的表（方便測試）"""
        return cls([cost] * 36)

    @classmethod
    def from_flat_string(cls, s):
        """從一行 36 個整數（空白分隔）建立成本表"""
        values = list(map(int, s.split()))
        return cls(values)

print("\n=== CPE：進位制成本計算 ===")
table = CostTable.uniform(1)
n = 255
for base in range(2, 11):
    c = table.total_cost(n, base)
    print(f"  255 在 {base:2d} 進位：位數 {c}")


