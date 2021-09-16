#Sam Fortuin, 99059050
#vars to use in calculations
ableToSpend = 88.0
amountOfTires = 2.0
tirePrice = 27.98
tireChangePrice = 15.0

#calculation for the total price & left over money
totalPrice = amountOfTires * (tirePrice + tireChangePrice)
leftOver = ableToSpend - totalPrice

#prints total price and left over money rounded to 2 decimal points in one statement
print("Total repair cost is €",round(totalPrice,2),"\nThis leaves you with €",round(leftOver,2))