# Collect information
Tip = .18
salesTax = .5


#Input Information
FoodCharge = float(input("Please enter the price of Meal: "))


#Calculations
Tip = .18 * FoodCharge
salesTax = .05 * FoodCharge
TotalPurchase = (FoodCharge + Tip + salesTax)




#Output
print("Food Charge", format(FoodCharge,",.2f"))

print("Amount of Tip", format(Tip,",.2f"))

print("Amount of Sales Taxs", format(salesTax,",.2f"))

print("Total purchased",format(TotalPurchase,",.2f"))

