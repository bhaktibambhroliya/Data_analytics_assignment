def remove_last_items(order):
    removed_items = order.pop()
    return removed_items

    order = ["pizza", "burger", "pasta"]

    removed = remove_last_items(order)

    print("Removed item:", removed)
    print("Updated order:", order)



