monthlyIncome = input("Enter your monthly income: ")
monthlyExpenses = input("Enter your total monthly expenses: ")

monthlySavings = int(monthlyIncome) - int(monthlyExpenses)
projectedSavings = monthlySavings*12 + (monthlySavings*12*0.05)

print("Projected savings after one year, with interest, is: ", projectedSavings)
