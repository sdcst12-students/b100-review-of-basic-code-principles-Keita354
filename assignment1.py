"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""
#python3
def CoSI():
  try:
    init=float(input("Enter initial investment"))

    an_rate=float(input("Enter annual interest rate %"))

    anrate_decimal = an_rate / 100.0

    timetype= (input("Enter type of time period (years, months or days)")).strip().lower()
    time = float(input("Enter length of time"))

    if timetype == 'months':
      time /= 12.0
  
    elif timetype == 'days':
     time /= 365.0
  
    interest = init * anrate_decimal * time

    print("simple Interest Calculation")
    print(f"Initial Investment amount (i): ${init:.2f}")
    print(f"Annual interest rate (r): {an_rate:.2f}%")
    print(f"Length of time (t): {time:.2f} years")
    print(f"Simple Interest (I) ${interest:.2f}")

  except ValueError:
    print("Error")

if __name__ == "__main__":
    CoSI()
