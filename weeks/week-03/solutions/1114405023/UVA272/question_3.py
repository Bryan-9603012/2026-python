def main():
    import sys

    # 用來記錄目前遇到的雙引號應該是開引號還是關引號
    # True 代表下一個 " 要換成 ``
    # False 代表下一個 " 要換成 ''
    open_quote = True

    # 逐行讀取輸入，直到 EOF
    for line in sys.stdin:
        result = []

        # 逐字檢查這一行
        for ch in line:
            if ch == '"':
                # 根據目前狀態決定要替換成開引號還是關引號
                if open_quote:
                    result.append("``")
                else:
                    result.append("''")

                # 每遇到一次雙引號，就切換狀態
                open_quote = not open_quote
            else:
                # 不是雙引號就原樣保留
                result.append(ch)

        # 輸出處理後的這一行
        print("".join(result), end="")


if __name__ == "__main__":
    main()