import sys

DOOMSDAY = [10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def weekday(month, day):
    return WEEKDAYS[(day - DOOMSDAY[month - 1]) % 7]

def solve(data):
    nums = list(map(int, data.split()))
    t = nums[0]
    out = []
    idx = 1
    for _ in range(t):
        month, day = nums[idx], nums[idx + 1]
        idx += 2
        out.append(weekday(month, day))
    return "\n".join(out)

print(solve(sys.stdin.read()))
