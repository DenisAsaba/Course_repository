numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0

for number in numbers:
    if number > 5:
        count = count + 1

print(count)

numbers = [6, 2, 3, 4, 5, 6, 10, 8, 9, 10]
total = 0

for number in numbers:
    total = total + number

print(total)


numbers = [6, 2, 3, 4, 5, 6, 10, 8, 9, 10]
find = None

for number in numbers:
    if number > 8:
        find = number
        break

print(find)