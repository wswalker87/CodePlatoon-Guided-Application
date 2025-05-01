# Today and for the rest of the course, we are going to build a lottery simulator that works almost exactly like the PowerBall or Mega-Millions.  If you haven't played the lottery before, here is a quick description of how it works:

# ### Where to Begin?

# Going back to the Problem Solving and Computational Thinking strategies we learned at the beginning of the course, how do we get started?

# Today we are going to explore the power of python and create something together. You can use this Jupyter Notebook to follow along & try your own solutions to the various problems we face while building this project!

# Today and for the rest of the course, we are going to build a lottery simulator that works almost exactly like the PowerBall or Mega-Millions. If you haven't played the lottery before, here is a quick description of how it works:

# PowerBall Lottery

# The Powerball lottery is a popular multi-state lottery game in the United States, known for its large jackpots and widespread participation. Players select five numbers from a set of 69 white balls and one number, the Powerball, from a set of 26 red balls. Drawings are held twice a week, typically on Wednesday and Saturday nights.

# To win the jackpot, a participant must match all five white ball numbers and the Powerball number. The odds of winning the jackpot are astronomical, at about 1 in 292.2 million, reflecting the game's design to build large jackpots that attract more players. However, the game also offers smaller prizes for matching fewer numbers, which have significantly better odds of winning.

# Ticket prices are generally $2 per play, and tickets can be purchased in most convenience stores and even online.
## ******* ##
# Ask our user to choose 5 white balls from 1-69. Be sure to change them to int type. # Function 1
import random

user_lotto_numbers = []
def user_numbers():
    #user_lotto_numbers = [] # commented out so that the number would get stored up in the global 
    counter = 0
    while len(user_lotto_numbers) < 5:
        user_choice = input(f'Hello User. Select your numbers. Choose from 1-69.   ')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < 1 or user_choice > 69:
                print(f'The number needs to be between 1 and 69')
            else:
                if user_choice not in user_lotto_numbers:
                    user_lotto_numbers.append(user_choice)
                else:
                    print(f'Hey! No duplicates allowed!')
        else:
           print(f"Hey, user, use a number!")
    print(f'You have chosen the following numbers: {user_lotto_numbers}')     
    powerball_number()
    return user_lotto_numbers
#[67, 5, 8, 32, 58]

def powerball_number():
    while len(user_lotto_numbers) < 6:
        user_pb_num = input(f'Now choose your winning powerball number! Choose from 1 to 26   ')
        if user_pb_num.isdigit():
            user_pb_num = int(user_pb_num)
            if user_pb_num < 1 or user_pb_num > 26:
                print(f'Powerball number must be between 1 and 26.')
            else:
                user_lotto_numbers.append(user_pb_num)
        else:
            print(f'Your powerball choice needs to be a number')
    print(f'You chose {user_lotto_numbers[5]} as your powerball number')
    winning_numbers()
    return user_lotto_numbers

def winning_numbers():
    print("I am inside winning numbers")
    winning_ball_numbers = []
    winning_pb_num = random.randint(1,26)
    while len(winning_ball_numbers) < 5:
        winning_wb_numbers = random.randint(1,69)
        winning_ball_numbers.append(winning_wb_numbers)
        #return winning_ball_numbers
    winning_ball_numbers.append(winning_pb_num)
    print(f'The winning numbers are: {winning_ball_numbers}')
    return winning_ball_numbers

print(user_numbers())
# once all number have been selected, generate the winning number using randint # Function # *

# generate a data structure that has our prize chart

# use a loop that's going to check out numbers against the winning numbers. 

# Display the message of winning or losing