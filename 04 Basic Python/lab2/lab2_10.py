cost = int(input("Enter food cost:"))
tip = int(input("Enter tip:"))
vat_cost = cost*1.07
total_cost = tip + vat_cost
print(f"Food cost with VAT (7%) is {vat_cost:.2f} baht.")
print(f"Total cost is {total_cost:.2f} baht.")
money = int(input("Enter money to pay:"))
change = money - total_cost
print(f"Change is {change:.2f} baht.")
change = int(change)

n100 = change // 100
change = change - n100*100 # change = change % 100 
n50 = change // 50
change = change % 50
print("100 baht:", n100) 
print("50 baht:", n50)
print("change", change)

