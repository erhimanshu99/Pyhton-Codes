def calculate_electricity_bill():
    customer_id = input("Enter customer ID: ")
    customer_name = input("Enter customer name: ")
    units_consumed = int(input("Enter units consumed: "))
    if units_consumed <= 199:
        charge_per_unit = 1.20
    elif 200 <= units_consumed < 400:
        charge_per_unit = 1.50
    elif 400 <= units_consumed < 600:
        charge_per_unit = 1.80
    else:
        charge_per_unit = 2.00
    total_bill = units_consumed * charge_per_unit
    if total_bill > 400:
        surcharge = total_bill * 0.15
        total_bill += surcharge
    total_bill = max(total_bill, 100)
    print("\nElectricity Bill")
    print("Customer ID:", customer_id)
    print("Customer Name:", customer_name)
    print("Units Consumed:", units_consumed)
    print("Charge per Unit: Rs.", charge_per_unit)
    print("Total Bill: Rs.", total_bill)
calculate_electricity_bill()
