total = int(input("Enter your zomato order total: "))

if total >299:
    print("apply free delivery")

elif total >= 200:
    print("add more item for free delivery")

else:
    print("delivery charges apply")