def even_numbers(lst):
    even_list = []

    for n in lst:
        if n % 2 == 0:
            even_list.append(n)

    return even_list


numbers = [1, 2, 3, 4, 5, 6]
print(even_numbers(numbers))
