try:
    monthlyIncome = float(input("Enter your monthly income: "))
    monthlyExpenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
    monthlySavings = monthlyIncome - monthlyExpenses

# calculating projected yealy savings
    yearlysavings = monthlySavings * 12
    projectedSavings = yearlysavings * 1.05

 # Display result formatted to 2 decimal places
    print(f"\nProjected savings after one year, with interest: ${projectedSavings:.2f}")

except ValueError:
    print("Invalid input, please enter numbers only")
