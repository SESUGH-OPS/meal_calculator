def calculate_total_meal_cost(charge_of_food):
    tip_percent = 18
    sales_tax_percent = 7

    tip_amount = charge_of_food * (tip_percent / 100)
    sales_tax_amount = charge_of_food * (sales_tax_percent / 100)
    total_amount = charge_of_food + tip_amount + sales_tax_amount

    return tip_amount, sales_tax_amount, total_amount

charge_of_food = float(input("Enter the charge of the food: "))
tip_amount, sales_tax_amount, total_amount = calculate_total_meal_cost(charge_of_food)

print(f"Tip: ${tip_amount:.2f}")
print(f"Sales tax: ${sales_tax_amount:.2f}")
print(f"Grand total: ${total_amount:.2f}")