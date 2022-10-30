loan = eval(input("請輸入貸款金額:"))
year = eval(input("請輸入年限:"))
rate = eval(input("請輸入年利率:"))
month_rate = rate / (12 * 100)

molecules = loan * month_rate
denominator = 1 - (1 / (1 + month_rate) ** (year * 12))
monthly_pay = molecules / denominator
total_pay = monthly_pay * year * 12

print("每月還款金額 %d" % int(monthly_pay))
print("總共還款金額 %d" % int(total_pay))