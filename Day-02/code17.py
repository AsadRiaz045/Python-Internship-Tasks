def sum_of_digits(num):
    total = 0

    for digit in str(num):
        total = total + int(digit)

    return total
number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
