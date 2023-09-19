"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

def debt():
    try:

        init_debt = float(input("Enter the initial debt: $"))
        an_int_rate = float(input("Enter the annual interest rate (%): "))
        month_pay = float(input("Enter the monthly payment: $"))

        month_int_rate = an_int_rate / 12.0 / 100.0

        months = 0
        total_interest_paid = 0.0

        while init_debt > 0:
            month_int = init_debt * month_int_rate

            total_pay = month_pay + month_int

            init_debt -= month_pay

            total_interest_paid += month_int

            months += 1

        print(f"It will take {months} months to pay off the debt.")
        print(f"Total interest paid: ${total_interest_paid:.2f}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    debt()