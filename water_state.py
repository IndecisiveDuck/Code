#solid below 32 f or 0 c
#liquid below 212 f or 100 c
#gas otherwise

validate = {'c', 'f'}
valid_input = False
while not valid_input:
    value = input("What temature messurment will you be working with? \n C/F ")
    valid_input = value.lower() in validate

messurment = value

tempature = float(input("what is the current tempeture? "))

if messurment == 'c':
    if tempature < 0:
        state = 'solid'
    elif tempature < 100:
        state = 'liquid'
    else:
        state = 'gas'
else:
    if tempature < 32:
        state = 'solid'
    elif tempature < 212:
        state = 'liquid'
    else:
        state = 'gas'

print(f"The tempature is {tempature}{messurment.upper()} and any water is {state}")