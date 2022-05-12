#import
import random

#array for the choices
computer_choices = ['rock', 'paper', 'scissor']

#welcoming statment + choices
print("Welcome to rock, paper and scissor")
#note to finish the game
print("note:to exit game write: quit / break / close / exit")
print("")

#while is used to loop the game 
while True:
    #random choice for computer
    random.shuffle(computer_choices)
    one_choice = random.choice(computer_choices)

    #user choice
    print("Your choice - ")
    user_choice = input()

    #rock == rock  tie
    if one_choice == "rock" and user_choice == "rock":
        print("Computer's choice - "+ one_choice)
        print("")
        print("!! Tie !!")

    #user(paper) > computer(rock)   "user win"
    elif one_choice == "rock" and user_choice == "paper":
        print("Computer's choice - "+ one_choice)
        print("")
        print("!! You Win !!")

    #user(scissor) < computer(rock)   "user lose"
    elif one_choice == "rock" and user_choice == "scissor":
        print("Computer's choice - "+ one_choice)
        print("")
        print("!! You lose !!")

    #user(rock) < computer(paper)   "user lose"
    elif one_choice == "paper" and user_choice == "rock":
        print("Computer's choice - "+ one_choice)
        print("")
        print("!! You lose !!")

    #paper == paper  tie
    elif one_choice == "paper" and user_choice == "paper":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Tie !!")

    #user(scissor) > computer(paper)   "user win"
    elif one_choice == "paper" and user_choice == "scissor":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! You Win !!")

    #user(rock) > computer(scissor)   "user win"
    elif one_choice == "scissor" and user_choice == "rock":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! You Win !!")

    #user(paper) < computer(scissor)   "user lose"
    elif one_choice == "scissor" and user_choice == "paper":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! You lose !!")

    #scissor == scissor  tie
    elif one_choice == "scissor" and user_choice == "scissor":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Tie !!")

    #End game
    elif 'quit' in user_choice or 'break' in user_choice or 'close' in user_choice or 'exit' in user_choice:
        print("")
        print("Thank You for playing !!!")
        break