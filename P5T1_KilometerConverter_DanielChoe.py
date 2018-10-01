# Convert kilometers to miles
# 10/1/18
# CTI-110 P5T1_KilometerConverter 
# Daniel Choe
#

Conversion_factor = 0.6214

def main():
    kilometers = float(input('Enter a distance in kilometers: '))

    show_miles(kilometers)

def show_miles(km):
    miles = km * Conversion_factor

    print(km, 'kilometers equals', miles, 'miles.')

main()
    
