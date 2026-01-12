n = int(input("Enter a number: "))

a = 0
b = 1

print("Fibonacci series:")

while a <= n:
    print(a)
    c = a + b
    a = b
    b = c
