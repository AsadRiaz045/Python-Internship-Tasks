# Original list with duplicates
numbers = [1, 2, 3, 2, 4, 1, 5]

# Empty list to store unique elements
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)  # add only if not already in list

print(unique_numbers)
