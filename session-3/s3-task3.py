price = [199.99, 299.50, 200]

float_prices = [float(p) for p in price]

total= sum(float_prices)

print("Float Price:", float_prices)
print("Total:", total)