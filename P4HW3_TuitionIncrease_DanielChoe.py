# Gives you how much tuition is at that given year
# 9/26/18
# CTI-110 P4HW3 - Tuition Increase
# Daniel Choe
#


tuition = 8000

# Start of loop
keep_going ='y'
while keep_going == 'y':
    # your variable(year)
    yearx = int(input('What year between 0-6: '))
    # your year is put into a formula
    moneyx = tuition*(1.03**yearx)
    # final answer into a format

    # number below 1 or above 5 will tell your number isnt between 0-6
    if yearx >= 6:
        print('The number is not between 0-6')

    elif yearx <= 0:
        print('The number is not between 0-6')

    else:
        print('Your tuition this year is $', format(moneyx, ',.2f'))

    keep_going = input('Want to reenter another a year (y/n): ')


# 1. You a variable(year)
# 2. the variable is put into a formula
# 3. final answer in currency format
# 4. if it doesnt follow the varaiable directions it will tell you error
