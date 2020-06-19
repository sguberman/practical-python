# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
month = 0

# Extra payments
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month in range(extra_payment_start_month, extra_payment_end_month):
        payment = base_payment + extra_payment
    else:
        payment = base_payment
    principal = principal * (1 + rate/12) - payment
    if principal < 0:
        payment += principal
        principal = 0
    total_paid = total_paid + payment
    month += 1
    print(f'{month:>3d} {total_paid:>10.2f} {principal:>10.2f}')

print('Total paid', round(total_paid, 2))
print('Months', month)
