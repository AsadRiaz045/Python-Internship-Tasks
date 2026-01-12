numbers = [1,4,5,5,5,5, 2, 2, 3, 4, 2, 5, 3, 3]

most_freq = numbers[0]
max_count = 0

for num in numbers:
    count = 0
    for n in numbers:
        if n == num:
            count += 1
    if count > max_count:
        max_count = count
        most_freq = num

print( most_freq)
