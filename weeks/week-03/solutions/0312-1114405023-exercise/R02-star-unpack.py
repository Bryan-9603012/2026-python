def drop_first_last (grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1234', '847-555-1212')
name, email, *phone_numbers = record

*trailing, current = [10,8,7,1,9,5,10,3]

print(drop_first_last([1,2,3,4,5]))
print(name)
print(email)
print(phone_numbers)
print(trailing)
