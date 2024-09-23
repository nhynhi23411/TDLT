def calculate_bill(customer_name, customer_group, kwh_used):
    bill = 0
    
    if customer_group == 1:
        if kwh_used <= 50:
            bill = kwh_used * 1549
        elif kwh_used <= 100:
            bill = 50 * 1549 + (kwh_used - 50) * 1600
        elif kwh_used <= 200:
            bill = 50 * 1549 + 50 * 1600 + (kwh_used - 100) * 1858
        elif kwh_used <= 300:
            bill = 50 * 1549 + 50 * 1600 + 100 * 1858 + (kwh_used - 200) * 2340
        elif kwh_used <= 400:
            bill = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + (kwh_used - 300) * 2615
        else:
            bill = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + 100 * 2615 + (kwh_used - 400) * 2701
    
    elif customer_group == 2:
        bill = kwh_used * 2271

    return f"Customer: {customer_name}, Total Bill: {bill} VND"

customer_name = input("Enter customer name: ")
customer_group = int(input("Enter customer group (1 for household, 2 for prepaid meters): "))
kwh_used = int(input("Enter kWh used: "))

print(calculate_bill(customer_name, customer_group, kwh_used))
