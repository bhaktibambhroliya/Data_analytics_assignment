def format_coupon_message(user_name, discount=10):
    return f"hi {user_name}, you get {discount}% off!"

print(format_coupon_message("Alice", 20))
print(format_coupon_message("priya"))