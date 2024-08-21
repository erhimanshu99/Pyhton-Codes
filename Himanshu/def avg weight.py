def calculate_average_weight():
    weight1 = float(input("Enter weight of item 1: "))
    quantity1 = float(input("Enter number of purchases for item 1: "))
    weight2 = float(input("Enter weight of item 2: "))
    quantity2 = float(input("Enter number of purchases for item 2: "))
    total_weight = (weight1 * quantity1) + (weight2 * quantity2)
    total_quantity = quantity1 + quantity2
    if total_quantity == 0:
        print("Error: Total quantity cannot be zero.")
    else:
        average_weight = total_weight / total_quantity
        print("Total Weight:",total_weight)
        print("Average Weight:",average_weight)
calculate_average_weight()