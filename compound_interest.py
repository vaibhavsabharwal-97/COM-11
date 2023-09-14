def calculate_compound_interest(principal, rate, time, compounding_frequency):
    
    rate = rate / 100

    amount = principal * (1 + rate / compounding_frequency) ** (compounding_frequency * time)

    interest = amount - principal

    return amount, interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the number of years: "))
compounding_frequency = int(input("Enter the compounding frequency (e.g., 12 for monthly): "))

final_amount, interest_earned = calculate_compound_interest(principal, rate, time, compounding_frequency)

print(f"Principal Amount: ${principal:.2f}")
print(f"Annual Interest Rate: {rate:.2f}%")
print(f"Time (years): {time}")
print(f"Compounding Frequency: {compounding_frequency} times per year")
print(f"Final Amount: ${final_amount:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")
