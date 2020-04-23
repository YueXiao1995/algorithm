income_increase_rate = 0.1
annual_income = 3 * 12
annualized_returns = 0.07
total_assets = 0
total_assets_without_fund = 0
available_proportion_of_investment = 0.75
previous = 0
emergency_fund = 0

for i in range(40):
    previous = total_assets
    total_assets = (total_assets + annual_income * (1 + i * income_increase_rate) * available_proportion_of_investment) * (1 + annualized_returns)
    total_assets_without_fund += annual_income * (1 + i * income_increase_rate) * available_proportion_of_investment
    emergency_fund += annual_income * (1 + i * income_increase_rate) * 0.25
    print(str(i) + " " + str(total_assets) + " " + str(total_assets_without_fund) + " " + str(total_assets - previous) +" " + str(emergency_fund))

a = (140 - 30) / 40
print(a)
