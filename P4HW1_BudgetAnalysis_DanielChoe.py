# 9/26/18
# CTI-110 P4HW1 - Budget Analysis
# Daniel Choe
# Show if your over or under our budget.

# You put your variable which will be the variable to define if your under, equal, or over.
budget = int(input("Enter your budget amount: "))

Final = 0

# Start of the loop
keep_going = 'y'

# You put your expenses, and if you says yes it will ask the same thing until you says no
while keep_going == 'y':
    
    expenses = int(input('Enter your expenses: '))

    keep_going = input('You want to add more expenses (Enter y/n): ')

    Final += expenses

amount = -(budget-Final)
amount2 = budget-Final

# Your total expenses will go to an if statement to show if its under, equal, or above your budget.
if budget < Final:
    print('Your over budget by $',amount,'This is your expenses that you have spent: $',Final,)

elif budget == Final:
            print("Your at the maximum budget")

else:
        print('Your under budget by $',amount2,'This is your expenses that you have spent: $',Final,)


# 1. You put a variable (your budget)
# 2. You put an amount to your expenses
# 3. It ask you if you have more, if so you click yes, if not then click no
# 4. The total of the expenses is put into a if statement and show you the difference and how much the total of expenses you spent.

