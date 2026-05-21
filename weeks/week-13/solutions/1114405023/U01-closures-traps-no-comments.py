def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))
print(add_to_cart("香蕉"))
print(add_to_cart("葡萄"))


print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_to_cart_safe("蘋果"))
print(add_to_cart_safe("香蕉"))


print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []
for i in range(5):
    funcs.append(lambda: i)

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])


print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")
funcs_ok = []
for i in range(5):
    funcs_ok.append(lambda i=i: i)

print("修正後：", [f() for f in funcs_ok])


print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """回傳一個計數器函數，每次呼叫加 1"""
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c1 = make_counter()
c2 = make_counter(10)
print(c1(), c1(), c1())
print(c2(), c2())
print(c1())


print("\n=== 閉包應用：記住已走過的節點 ===")
def make_visit_tracker():
    visited = set()

    def visit(node):
        nonlocal visited
        if node in visited:
            return False
        visited.add(node)
        return True

    return visit

visit = make_visit_tracker()
results = [visit(n) for n in [1, 2, 1, 3, 2, 4]]
print(results)


