AI_USAGE.md
# AI Usage

## 我問 AI 的問題

1. 如何保持 list 去重但不破壞順序
2. Python sorted 多條件排序怎麼寫
3. defaultdict 與 Counter 的差異
4. 如何撰寫 unittest 測試案例
5. 如何設計邊界測試

---

## 我採用的建議

- 使用 set + list 方式實作 dedupe
- 使用 sorted(key=lambda ...) 實作多條件排序
- 使用 Counter 統計 action 次數

---

## 我拒絕的建議

AI 曾建議使用 `set(nums)` 直接去重，  
但這會破壞原本的順序，因此沒有採用。

---

## AI 可能誤導的案例

AI 初期給的排序 key 為：


key=lambda x: (x[1], x[2], x[0])


這會讓 score 由小到大排序，  
與題目要求的由大到小不符。

最後修正為：


key=lambda x: (-x[1], x[2], x[0])