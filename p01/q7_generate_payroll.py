name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
pay_rate = int(input("Enter hourly pay rate: "))
CPF = int(input("Enter CPF contribution rate(%): "))
gross_pay = hours * pay_rate
CPF_contribution = gross_pay * (CPF / 100)
net_pay = gross_pay - CPF_contribution

print("Payroll statement for", name)
print("Number of hours worked in week:", hours)
print("Hourly pay rate:", pay_rate)
print("Gross pay =", gross_pay)
print("CPF contribution at 20%:", CPF_contribution)
print("Net pay =", net_pay)
