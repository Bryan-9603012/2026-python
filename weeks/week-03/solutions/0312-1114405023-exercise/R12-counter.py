from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)
word_counts.most_common(3)

word_counts.update(['eyes','eyes'])

print(word_counts['eyes'])