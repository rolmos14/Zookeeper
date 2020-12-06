deposit = int(input())
interest_rate = 7.1 / 100
max_deposit = 700000
years = 0

while deposit < max_deposit:
    deposit += (deposit * interest_rate)
    years += 1

print(years)
