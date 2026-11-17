def total_calc(bill_amount, tip_perc):
    total= bill_amount + (bill_amount * tip_perc)
    total= round(total, 20)
    print("Your total bill is: $", total)

total_calc(12,2)