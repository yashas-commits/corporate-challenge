p = float(input("Enter loan amount: "))
r = float(input("Enter annual interest rate (%): ")) / 12 / 100
n = int(input("Enter loan duration in months: "))

emi = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)

print("Monthly EMI =", round(emi, 2))
print("Total Payment =", round(emi * n, 2))
#thank you 
