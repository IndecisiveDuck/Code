
#Letter work
letter_length_inch = 8.5
letter_width_in = 11

conversion_to_mil = 25.4

letter_length_mi = letter_length_inch * conversion_to_mil
letter_width_mil = letter_width_in * conversion_to_mil

print(f"{letter_length_mi} x {letter_width_mil}")

#Poem work
print("That's right, I'm Sokka,")
print("It's pronounced with an 'okka',")
print("Young ladies, I rocked ya!")
print("-Sokka of the southern watertribe")


#Gas vroom
print("How many gallons per tank? ")
gallons_in_tank = 15.9 #float(input())
print("What is the fuel effiency?")
miles_per_gallon = 21 #float(input())
print("Price of gas?")
stupid_gas_price = 4.09 #float(input())
print("How many miles?")
mile_to_travel = 100 #float(input())

# Calculate cost to drive 100 miles


#gallons needed to travel
gallons_needed = mile_to_travel / miles_per_gallon
#How many times needed to refuel
refills_needed = gallons_needed / gallons_in_tank
#how much to spend
emptying_wallet = gallons_needed * stupid_gas_price
print(f"You will spend around ${emptying_wallet}")
