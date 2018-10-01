# Show how many inches are in that number of foots
# 10/1/18
# CTI-110 P5T2_FeetToInches 
# Daniel Choe
#

Inches_per_foot = 12

def main ():
    feet = int(input('Enter a number of feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches')

def feet_to_inches(feet):
    return feet * Inches_per_foot

main()
               
