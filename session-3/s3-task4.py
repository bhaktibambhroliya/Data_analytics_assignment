def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False

print("450:", is_discount_applicable(450))
print("750:", is_discount_applicable(750))