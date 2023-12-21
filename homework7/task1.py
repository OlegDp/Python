suma = float(input("Введіть суму кредиту: "))

annual_interest_rate = 0.02  
payment_duration_years = [1, 5]

print("Розрахунок на 1 рік - перші 12 місяців. Розрахунок на 5 років - наступні 60.")
print("{:<10} {:<20} {:<20}".format("Місяць", "Сума виплати", "Проценти"))

for duration in payment_duration_years:
    total_payments = duration * 12
    current_balance = suma
    print()

    for month in range(1, total_payments + 1):
        if month <= 24:
            monthly_procent = 0.02
        else:
            monthly_procent = 0.04

        procent_payment = current_balance * monthly_procent
        monthly_payment = suma * (monthly_procent / (1 - (1 + monthly_procent) ** -total_payments))
        principal_payment = monthly_payment - procent_payment

        current_balance -= principal_payment

        print("{:<10} {:<20.2f} {:<20.2f}".format(month, monthly_payment, procent_payment))
