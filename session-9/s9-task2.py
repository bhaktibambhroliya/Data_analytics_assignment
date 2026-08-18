def get_delivery_charge(amount, city="Ahemdabad"):
    if city == "Ahemdabad":
        return 30
    else:
        return 50

print("Ahemdabad:", get_delivery_charge(500))
print("Mumbai:", get_delivery_charge(500, "Mumbai"))