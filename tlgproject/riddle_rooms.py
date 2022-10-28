#!/usr/bin/python3
"""TLG Project | Shalese Childress
	Riddle Rooms"""

from art import *


def showInstructions():
    """Show the game intro"""
    #print a main menu and the commands
    
    tprint('''
    
    Riddle Space
    =========''')
    print('''The GOAL is to make it back to EARTH''')

    print('''Commands:
      go [direction] 
    ''')

def showStatus():
    """current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are on ' + currentRoom)
    # print what the user must do to return
    print('You must answer riddles correctly to navigate back to Earth')
    # if there is an item in the room print the riddle
    if "item" in rooms[currentRoom]:
      print('You are on ' + currentRoom)
    print("---------------------------")

# create a class for riddles for reference in loop
class Question:
    def __init__(self, questionText, answer):
        self.questionText = questionText
        self.answer = answer

    # represent the riddle as a string
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +'}'

# create a list of riddles for specific planets
itemQuestions = [
    Question("Riddle 1. I can be full even though I haven\'t eaten anything", "Moon")]

itemQuestionsB = [
    Question("Riddle 2. I am a red planet, but almost never warm", "Mars")]

itemQuestionsC = [
    Question("Riddle 3. I have many rings, but never been married", "Saturn")
]


# a dictionary linking a room to other rooms
rooms = {

            'Unknown Moon' : {
                  'east' : 'Venus'
                },

            'Venus' : {
                  'west' : 'Unknown Moon',
                  'south' : 'Mercury',
                },

            'Mercury' : {
                  'west' : 'Earth',
                  'north' : 'Venus',
                  'item' : itemQuestions
                },

            'Earth' : {
                  'east' : 'Mercury'
         }

     }

# start the player on the Unknown Moon
currentRoom = 'Unknown Moon'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # user will type in direction they move in
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list          
    move = move.lower().split(" ", 1)


    # if they type 'go' first
    if move[0] == 'go':
                #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('Wrong way!')

    ## if you land on a planet with a riddle
    if 'item' in rooms[currentRoom]:
        # link question and prompt riddle:
        for question in itemQuestions:
            print(f"{question.questionText}?")
            # user input answer
            userChoice = input()
            if (userChoice.lower() == question.answer.lower()):
            # if correct move to the next planet
                print("That is correct!")
            else:
                print('Wrong')
            break

    ## Define how a player can win
    if currentRoom == 'Earth':
        print('You have made it back to earth!')
        break
