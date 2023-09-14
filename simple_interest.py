def calculate_simple_interest(principal, rate, time):

    rate = rate / 100

    interest = principal * rate * time

    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the number of years: "))

interest = calculate_simple_interest(principal, rate, time)

print(f"Principal Amount: ${principal:.2f}")
print(f"Annual Interest Rate: {rate:.2f}%")
print(f"Time (years): {time}")
print(f"Simple Interest: ${interest:.2f}")
