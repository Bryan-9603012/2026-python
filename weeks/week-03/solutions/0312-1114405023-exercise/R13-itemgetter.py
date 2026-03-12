from operator import itemgetter

rows = [
    {'fname': 'Brian','uid': 1003},
    {'fname': 'Jhon','uid': 1001},]
sorted(rows, key=itemgetter('fname'))
sorted(rows, key=itemgetter('uid'))
sorted(rows, key=itemgetter('uid','fname'))

print(rows)
print(sorted(rows, key=itemgetter('fname')))
print(sorted(rows, key=itemgetter('uid')))
print(sorted(rows, key=itemgetter('uid','fname')))