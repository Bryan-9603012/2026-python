# U02.py
# 範例：星號解包 (extended unpacking)
# 當元素數量不確定時，*var 會收集剩餘元素成 list

record = ('Dave', 'dave@example.com')
name, email, *phones = record
# phones == []  仍是 list
print("星號解包為何能處理「不定長」且結果固定是 list")