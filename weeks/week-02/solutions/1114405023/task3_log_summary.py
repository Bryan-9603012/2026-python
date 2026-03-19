from collections import defaultdict, Counter


def log_summary(records):
    user_count = defaultdict(int)
    action_counter = Counter()

    for user, action in records:
        user_count[user] += 1
        action_counter[action] += 1

    user_sorted = sorted(
        user_count.items(),
        key=lambda x: (-x[1], x[0])
    )

    top_action = None
    if action_counter:
        top_action = action_counter.most_common(1)[0]

    return user_sorted, top_action


def main():
    m = int(input())

    records = []
    for _ in range(m):
        user, action = input().split()
        records.append((user, action))

    users, top = log_summary(records)

    for u, c in users:
        print(u, c)

    if top:
        print("top_action:", top[0], top[1])


if __name__ == "__main__":
    main()