loan = float(input("enter amount"))
years = int(input("enter years to pay"))
month = years * 12
principal = loan / month
remaining_total = loan
for x in range (1, month + 1):
    print(x, round(principal, 2)) , round(remaining_total, 2)
    remaining_total -= principal
    loan_interest = remaining_total * 0.00256
    month = principal + loan_interest
    print ("x round(loan_interest, 2 ), round(principal, 2) round (remaining_total, 2")
    print(f" {x} \t | {month} \t | \t {loan_interest} \t | \t {principal} \t | \t {remaining_total}")
#monthly_pay = 40