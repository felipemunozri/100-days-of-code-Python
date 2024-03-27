## Mi codigo inicio
# print("Welcome to the tip calculator")
# bill_total = float(input("What was the total bill? $"))
# num_people = int(input("How many people to split the bill? "))
# tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# bill_with_tip = bill_total + (bill_total * (tip_percent / 100))
# result = str("{:.2f}".format(bill_with_tip / num_people))
# print("Each person should pay: $" + result)

## Mi codigo final
# print("Welcome to the tip calculator")
# bill_total = float(input("What was the total bill? $"))
# num_people = int(input("How many people to split the bill? "))
# tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# # bill_with_tip = bill_total + (bill_total * (tip_percent / 100))
# bill_with_tip =  tip_percent / 100 * bill_total + bill_total
# result = str("{:.2f}".format(bill_total / num_people))
# print(f"Each person should pay: ${result}")

## Respuesta
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# bill_with_tip = bill_total + (bill_total * (tip_percent / 100))
bill_with_tip =  tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")