# 檔案：字符串格式化練習
# 學習Python中的字符串格式化方法（f字符串和format方法）

# 定義變量
name = "Alice"
price = 91.1

# 方法1：使用f字符串（Python 3.6+推薦方法）
# {price:.2f} 表示將price格式化為小數點後2位
text = f'{name} price = {price:.2f}'
print(text)  # 輸出: Alice price = 91.10

# 方法2：使用format()方法（Python 3之前的方式）
# {} 表示佔位符，:.2f 表示格式化為小數點後2位
text2 = '{} price = {:.2f}'.format(name, price)
print(text2)  # 輸出: Alice price = 91.10