num = input("Enter a number: ")
reverse = ""
for digit in num:
    reverse = digit + reverse
if num == reverse:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
