#a personal program to randomly choose a strategy to use during a match of BF2042

# import the random module
import random

# create a list of strings to hold the strategies
strategies = ['sniper', 'assault', 'engineer', 'support']

# generate a random number between 0 and 3 to choose a strategy
choice = random.randint(0,3)

# print the strategy chosen
print("You should use the " + strategies[choice] + " class.")