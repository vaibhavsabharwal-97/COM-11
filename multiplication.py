num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Original numbers: num1 = {num1}, num2 = {num2}")

num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print(f"After swapping: num1 = {num1}, num2 = {num2}")
