import sys

tokens = sys.stdin.read().replace("=", " ").split()
t = int(tokens[0])
idx = 1

for case_id in range(1, t + 1):
    if tokens[idx] == "N":
        idx += 1
    n = int(tokens[idx])
    idx += 1
    values = list(map(int, tokens[idx:idx + n * n]))
    idx += n * n

    ok = True
    l, r = 0, len(values) - 1
    while l <= r:
        if values[l] < 0 or values[r] < 0 or values[l] != values[r]:
            ok = False
            break
        l += 1
        r -= 1

    print(f"Test #{case_id}: {'Symmetric.' if ok else 'Non-symmetric.'}")
