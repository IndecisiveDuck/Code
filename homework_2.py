#car cost
car_price = float(input("What's the cost of your car? "))
miles_per_year = float(input("How many miles do you drive per year? "))
cost_per_gallon = float(input("What is the cost of gas per gallon? "))
miles_per_gallon = float(input("What is the car's fuel efficiency in miles per gallon? "))
total_gallons_used = miles_per_year // miles_per_gallon
gas_bought = total_gallons_used * cost_per_gallon
final_total = (gas_bought * 5) + car_price

print(f"The five year cost of owning this car is {final_total}")

#Meters to 'Merica (caw)
MILES = 1609 #DIVIDE THIS PLS
FOOT = 3.281 #MULTIPLY
INCH = 39.37
meters_initial = int(input("Enter a distance in meters: "))
meters_to_miles = meters_initial / MILES
meters_to_feet = meters_initial * FOOT
meters_to_inches = meters_initial * INCH
print(f"{meters_initial} is equal to {meters_to_miles} miles, which is the same as {meters_to_feet} feet or {meters_to_inches} inches.")

#Idk what to call this
outside_string = input("Enter string: ")
inside_string = input("Enter another string: ")
half_string = len(outside_string)//2

#[inclusive:exclusive]
print(f"{outside_string[:half_string]}{inside_string}{outside_string[half_string:]}")