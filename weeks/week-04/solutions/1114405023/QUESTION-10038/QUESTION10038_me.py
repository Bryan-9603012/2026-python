def solve():
    import sys

    for line in sys.stdin:
        data = list(map(int, line.split()))
        n = data[0]
        arr = data[1:]

        if n == 1:
            print("Jolly")
            continue

        diff = set()

        for i in range(1, n):
            d = abs(arr[i] - arr[i-1])
            diff.add(d)

        if diff == set(range(1, n)):
            print("Jolly")
        else:
            print("Not jolly")