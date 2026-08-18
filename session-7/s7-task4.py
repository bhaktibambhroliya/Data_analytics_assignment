cart_value = int(input("Enter your flipkart cart value: "))
payment = input("Enter your payment method (UPI/card/cash): ")

if cart_value > 1000:
    if payment == "UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")