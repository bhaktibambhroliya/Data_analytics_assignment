followers = int(input("Enter the number of followers: "))

if followers < 10000:
    print("Micro Influencer")

elif followers <= 100000:
    print("Rising Star")

else:
    print("Celebrity")