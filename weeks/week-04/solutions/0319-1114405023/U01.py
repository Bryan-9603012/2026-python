# U01.py
# 範例：序列解包（unpacking）的錯誤原因示範
# 變數數量必須與待解包元素數量一致，否則會拋 ValueError

p = (4, 5)
# x, y, z = p  # 若解除註解，會出現 ValueError 因為只有兩個元素
print("解包失敗的原因：變數數量 ≠ 元素數量")