def main():
    import sys

    # True 表示下一個雙引號要換成開引號 ``
    # False 表示下一個雙引號要換成關引號 ''
    is_open_quote = True

    # 題目輸入有很多行，要一路讀到 EOF
    for line in sys.stdin:
        new_line = ""

        # 逐字處理
        for ch in line:
            if ch == '"':
                # 如果目前是開引號，就替換成 ``
                if is_open_quote:
                    new_line += "``"
                else:
                    # 否則替換成 ''
                    new_line += "''"

                # 每遇到一個雙引號就切換狀態
                is_open_quote = not is_open_quote
            else:
                # 不是雙引號就原樣保留
                new_line += ch

        # 因為 line 本身就有換行，所以這裡不要再多印一個換行
        print(new_line, end="")


if __name__ == "__main__":
    main()