cost = int(input("Enter food cost:"))
tip = int(input("Enter tip:"))
vat_cost = cost*1.07
total_cost = tip + vat_cost
print(f"Food cost with VAT (7%) is {vat_cost:.2f} baht.")
print(f"Total cost is {total_cost:.2f} baht.")