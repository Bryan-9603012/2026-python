from collections import deque

q  = deque(maxlen=3)
q.append(1);q.append(2);q.append(3)
q.append(4)

q= deque()
q.append(1);q.append(2)
q.pop(); q.popleft()

print(q)
print(len(q))
print(1 in q)
print(2 in q)
print(list(q))
print(list(reversed(q)))
print(q.count(1))
print(q.count(2))
