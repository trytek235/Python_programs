import random
import time

gests = ('rock', 'scissor', 'paper')

def computer_random():
    rad = random.randrange(3)
    return rad

def user_win():
    print("User win!")

def computer_win():
    print("Computer win!")

def draw():
    print("Draw!")

def user_gest_number(x):
    return gests.index(x)

def who_win(user, comp):
    if(user == 0 and comp == 2):
        user_win()
    elif(user == 2 and comp == 0):
        computer_win()
    elif(user<comp):
        user_win()
    elif(comp<user):
        computer_win()
    else:
        draw()



while(True):
    user_gest = input("Type rock, scissor or paper: ")
    computer_gest = computer_random()
    print("Computer choose: ", gests[computer_gest])
    print("...")
    time.sleep(2)
    who_win(gests.index(user_gest), computer_gest)
    time.sleep(2)
    print("")
    print("Let's play again!")