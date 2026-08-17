price = input("Enter zometo order price: ")

price = float(price)

gst = price * 18/100
final_price = price + gst

print("GST Amount:", gst)
print("Final Price:", final_price)