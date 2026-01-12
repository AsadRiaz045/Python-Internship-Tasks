num = int(input("Enter a number: "))

root = int(num ** 0.5)

if root * root == num:
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")
