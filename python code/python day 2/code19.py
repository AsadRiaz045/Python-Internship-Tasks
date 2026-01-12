def gcd(a, b):
    smaller = a if a < b else b

    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD is:", gcd(num1, num2))
