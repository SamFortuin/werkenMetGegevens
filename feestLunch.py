#99059050, Sam Fortuin
#vars for calculations
amountOfCroissants = 17.0
croissantsPrice = 0.39
amountOfBaguette = 2.0
baguettePrice = 2.78
couponSavings = 0.50
couponAmount = 3.0

lunchPrice = (amountOfCroissants * croissantsPrice) + (amountOfBaguette * baguettePrice) - (couponSavings * couponAmount)
print("Total price for the lunch is €",lunchPrice)