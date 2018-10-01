# Rock, paper, scissor
# 10/1/18
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Daniel Choe
#

import random
# Your input
hooman = input('Pick between rock, paper, scissor: ')

# random generator
cpu = random.randint(1, 3)

# you pick out of the 3 choices and the cpu pick randomly of the 3 choices
if hooman == 'scissor':
    if cpu == 1:
        print('Cpu chose rock so you lost')
    elif cpu == 2:
        print('Cpu chose paper so you lost')
    else:
        print('Draw')
        
elif hooman == 'paper':
    if cpu == 1:
        print('Cpu chose rock so you won')
    if cpu == 2:
        print('Draw')
    else:
        print('Cpu chose scissor so you lost')
elif hooman == 'rock':
    if cpu == 1:
        print('Draw')
    elif cpu == 2:
        print('Cpu chose paper so you lost')
    else:
        print('Cpu chose paper so you won')
else:
    print("You mistype your choice or it's not available")


# 1. Pick one of the 3 choices
# 2. Cpu randomly pick a number 1-3
# 3. Your choice will be in an if statement and the cpu random number will tell u if u lost or not.
    
