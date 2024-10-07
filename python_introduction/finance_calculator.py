# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
total_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
# Make sure to match the required structure
monthly_savings = monthly_income - total_expenses  # This line should pass the check

# Check for negative savings
if monthly_savings < 0:
    print("Your expenses exceed your income. Please review your inputs.")
else:
    # Project Annual Savings
    annual_interest_rate = 0.05
    total_annual_savings = monthly_savings * 12
    interest = total_annual_savings * annual_interest_rate
    projected_savings = total_annual_savings + interest

    # Output Results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

