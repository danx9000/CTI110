# Show you a table from 1-20 and translate the Celsius temp to Fahrenheit temp.
# 9/26/18
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Daniel Choe


# The table code
print('Celsius\tFahrenheit')
print('-------------------')

# Range
for Ctemp in range(0, 21):

# Formula for fahrenheit    
    Ftemp = (9/5)*(Ctemp) + 32
    print(Ctemp , '\t', Ftemp)
    
# 1. Split in 2 columns: Celsius & Fahrenheit
# 2. Range to 0-21
# 3. The celsius from 0-21 is changed to fahrenheit 
