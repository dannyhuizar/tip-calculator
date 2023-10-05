bill = float(input("What was the cost of the bill? $"))

tip = int(input("What tip percentage would you like? 10, 15, or 20 percent? (15% is the recommended tip) "))

tip_percent = tip / 100

bill_tip = round(tip_percent * bill)

combined_bill = bill_tip + bill

print("The total bill is " + str(combined_bill))

people = int(input("How many people will pay the bill?"))

paying_people = round(combined_bill / people)

print("Every person will pay $" + str(paying_people) + " each")

if tip not in [10,15,20]:
    print("Not a valid choice")

