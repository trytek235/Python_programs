import random
import time

gests = ('rock', 'paper', 'scissor')

def computer_random():
    rad = random.randrange(3)
    return gests[rad]

def user_win():
    print("User win!")

def computer_win():
    print("Computer win!")

def draw():
    print("Draw!")



while(True):
    user_gest = input("Type rock, scissor or paper: ")
    computer_gest = computer_random()
    print("Computer choose: ", computer_gest)
    print("...")
    time.sleep(2)
    if(user_gest==gests[0] and computer_gest==gests[2]):
        user_win()
    elif(user_gest==gests[0] and computer_gest==gests[1]):
        computer_win()
    elif(user_gest==gests[0] and computer_gest==gests[0]):
        draw()
    elif(user_gest==gests[1] and computer_gest==gests[0]):
        user_win()
    elif(user_gest==gests[1] and computer_gest==gests[1]):
        draw()        
    elif(user_gest==gests[1] and computer_gest==gests[2]):
        computer_win()
    elif(user_gest==gests[2] and computer_gest==gests[0]):
        computer_win()
    elif(user_gest==gests[2] and computer_gest==gests[1]):
        user_win()
    elif(user_gest==gests[2] and computer_gest==gests[2]):
        draw()
