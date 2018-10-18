def print_order(product, order_amount):
    print("Thank you for ordering the", product + '.')

    if order_amount >= 30:
        print("It's your lucky day! There is no shipping charge for orders over $30.00.")
    else:
        print("There will be a $5.00 shipping charge for this order.")

product1 = "Hanging Planter"
print_order(product1, 35)
print_order("Royal Visit Ash Tray", 4)
