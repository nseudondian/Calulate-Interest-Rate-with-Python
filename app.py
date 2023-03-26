def main():
    print("Calculate Your Monthly Loan Repayment")
    print("")

    principal = float(input("Enter loan amount: "))
    apr = float(input("Enter annual interest rate: "))
    years = int(input("Enter number of years: "))

    monthly_interest_rate = apr/1200
    number_of_months = years * 12
    monthly_repayment = principal * monthly_interest_rate / (1-(1+monthly_interest_rate) ** (- number_of_months))

    print(" The monthly repayment amount is: %.2f" % monthly_repayment)

main()
