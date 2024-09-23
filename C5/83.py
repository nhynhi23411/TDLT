def calculate_electricity_bill(old_reading, new_reading, num_households, bill_type):
  consumption = new_reading - old_reading
  total_consumption = consumption * num_households

  if bill_type.lower() == "laddered":
    if total_consumption <= 50 * num_households:
      bill = total_consumption * 1484
    elif total_consumption <= 100 * num_households:
      bill = (50 * num_households * 1484) + ((total_consumption - 50 * num_households) * 1533)
    elif total_consumption <= 200 * num_households:
      bill = (50 * num_households * 1484) + (50 * num_households * 1533) + ((total_consumption - 100 * num_households) * 1786)
    elif total_consumption <= 300 * num_households:
      bill = (50 * num_households * 1484) + (50 * num_households * 1533) + (100 * num_households * 1786) + ((total_consumption - 200 * num_households) * 2242)
    elif total_consumption <= 400 * num_households:
      bill = (50 * num_households * 1484) + (50 * num_households * 1533) + (100 * num_households * 1786) + (100 * num_households * 2242) + ((total_consumption - 300 * num_households) * 2503)
    else:
      bill = (50 * num_households * 1484) + (50 * num_households * 1533) + (100 * num_households * 1786) + (100 * num_households * 2242) + (100 * num_households * 2503) + ((total_consumption - 400 * num_households) * 2587)
  elif bill_type.lower() == "business":
    bill = consumption * 2320
  elif bill_type.lower() == "production":
    bill = consumption * 1518
  else:
    raise ValueError("Invalid bill type. Please choose Laddered, Business, or Production.")

  return bill

#
old_reading = int(input("Old reading: "))
new_reading = int(input("New reading: "))
bill_type1 = input("Input type laddered/business/production : ")
if bill_type1 == "laddered":
  num_households = int(input("Number households: "))
else:
  num_households = 1
  
electricity_bill = calculate_electricity_bill(old_reading, new_reading, num_households, bill_type1)
print(f"The electricity bill for {bill_type1} is: ${electricity_bill:.2f}")