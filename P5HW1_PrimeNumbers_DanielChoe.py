# This program tells if your number is a prime or not
# 10/1/18
# CTI-110 P5HW1 - Prime Numbers
# Daniel Choe
#


def main():
    # Your variable
    number = int(input('Put a number through 1-100: '))
    if number < 0:
        print('The number you chose is not through 1-100')
    # Checking if it is between 1-100
    elif number > 100:
        print('The number you chose is not through 1-100')
    else:
        # The if statement
        if is_prime(number):
            print('This is a non prime number')
        else:
            print('This is a prime numnber')
    

def is_prime(number):
    # return status 
    if (number % 2) == 0:
        status = True
    else:
        status = False
    return status
main()

# 1. Put your number
# 2. make sure if the number is through 1-100
# 3. the number goes into an if statement to see if it is prime or not
