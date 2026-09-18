#Culinary units
#ask the user to input a quanity ask for units and units to convert to
#(oz, tsp, tbsp, cup, gallons, qrtz)
#print conversion
#3 tsp -> 1 tbsp
#2 tbsp -> 1 oz -> 1/8 cup
#1 cup -> 8 oz
#1 gal -> 16 cups

quanity = float(input("Enter a quanity: "))

from_units = input("In what units (oz, tsp, tbsp, cup, gallons, qrtz)? ")
to_units = input("To what units (oz, tsp, tbsp, cup, gallons, qrtz)? ")

if from_units == "tsp" or from_units == "tbsp" and to_units == "tsp" or to_units == "tbsp":
    conversion = 3
elif from_units == "tbsp" or from_units == "oz" and to_units == "tbsp" or to_units == "oz":
    conversion = 2
elif from_units == 

print(to_units == "tsp" or "tbsp")