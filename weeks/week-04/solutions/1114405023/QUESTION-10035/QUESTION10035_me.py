def solve():
    while True:
        a, b = input().split()
        if a == '0' and b == '0':
            break

        a = a[::-1]
        b = b[::-1]

        carry = 0
        count = 0

        for i in range(max(len(a), len(b))):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0

            if x + y + carry >= 10:
                carry = 1
                count += 1
            else:
                carry = 0

        if count == 0:
            print("No carry operation.")
        elif count == 1:
            print("1 carry operation.")
        else:
            print(f"{count} carry operations.")