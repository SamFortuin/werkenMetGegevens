#99059050, Sam Fortuin

#vars
entreeCost = 7.45
amountOfBoys = 4.0
vrGameSeatPer5m = 0.37


#gameseat session lasts 45min so var vrGameSeatPer5m needs to be multiplied by 9
totalCost = (entreeCost * amountOfBoys) + ((vrGameSeatPer5m * 9) * amountOfBoys)
#print("The total cost for a day with the boys is €",round(totalCost,2))
print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar",round(totalCost,2),"euro")