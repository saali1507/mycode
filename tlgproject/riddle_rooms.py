#!/usr/bin/python3
"""TLG Project | Shalese Childress
	Riddle Rooms"""

import art
from art import tprint

def show_instructions():
    """Show the game intro"""
    #print a main menu and the commands

    tprint('''
    Riddle Space
    =========''')
    print('''You must solve riddles to return to earth''')
    print('''Commands:
      go [direction] 
    ''')

def show_status():
    """current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are on ' + currentRoom)
    print('---------------------------')
    # print what the user must do to return

rooms = {

            'Unknown Moon' : {
                  'east' : 'Venus'
                },

            'Venus' : {
                  'west' : 'Unknown Moon',
                  'south' : 'Mercury'
                },

            'Mercury' : {
                  'west' : 'Earth',
                  'north' : 'Venus',
                  'east' : 'Jupiter'
                },
            'Jupiter' : {
                  'west' : 'Mercury'
                },
            'Earth' : {
                  'east' : 'Mercury'
         }

     }

show_instructions()

# start the player on the Unknown Moon
currentRoom = 'Unknown Moon'

# breaking this while loop means the game is over
while True:
    show_status()

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
            currentRoom = 'Unknown Moon'

    ## if you land on a planet with a riddle
    if currentRoom == 'Venus':
        # link question and prompt riddle:
        print("Answer the riddle: I never eat but I am sometimes full")
        # user input answer
        answer = input()
        if answer.lower() == 'moon':
        # if correct move to the next planet
            print("That is correct!")
        else:
            print('Wrong You must return to Unknown Moon')
            currentRoom = 'Unknown Moon'

    if currentRoom == 'Mercury':
        # link question and prompt riddle:
        print("Answer the riddle: I have many rings but I have never been married")
        # user input answer
        answer = input()
        if answer.lower() == 'saturn':
        # if correct move to the next planet
            print("That is correct!")
        else:
            print('Wrong')

    ## Define how a player can win
    if currentRoom == 'Earth':
        print('You have made it back to earth!')
        break
