person_name = input("Enter your name: ")
person_sales = input("Enter your sales: ")

#  if person sales is empty then assign 0 to it
if person_sales == "":
    person_sales = 0

#  if person sales is not empty then convert it to float
else:
    person_sales = float(person_sales)

#  calculate 13% of sales
commission = person_sales * 0.13
print(f"Hello {person_name}! Your commission is {round(commission, 2)}")
