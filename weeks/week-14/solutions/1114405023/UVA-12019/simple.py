import sys

doomsday = [10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

t = int(sys.stdin.readline())
for _ in range(t):
    month, day = map(int, sys.stdin.readline().split())
    print(weekdays[(day - doomsday[month - 1]) % 7])
