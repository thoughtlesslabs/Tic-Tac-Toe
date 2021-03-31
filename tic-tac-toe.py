import random
import os
from time import sleep

playing = True
computer_turn = True
board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
winner = [0,1]

# Check to see if there are 3 x's in a row
# Need to add check fo Os
def check_for_win():
    wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    for x,y in board.items():
        if y == 'X':
            for i in wins:
                if x not in i:
                    pass
                else:
                    i.remove(x)
    for b in wins:
        if not b:
            return True

# Player gets to choose position, which must be empty
def player_move():
    global player_go
    player_go = True
    choice = int(input('Choose a location from 1 - 9: '))
    while player_go:
        if choice == 10:
            exit()
        elif board[choice] != ' ':
            choice = int(input('Pick a unoccupied spot: '))
        else:
            board.update({choice:'X'})
            player_go = False
    return player_go

# Automated computer move.
# Needs AI
def computer_move():
    global computer_turn
    computer_turn = True
    while computer_turn:
        pick_spot = random.randint(1,9)
        if board[pick_spot] != ' ':
            pick_spot = random.randint(1,9)
        else:
            board.update({pick_spot:'O'})
            computer_turn = False
    return computer_turn

# Print Game Board
def print_game():
    os.system('clear')
    print('        2\n')
    print('1   ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '   3')
    print('    ---------')
    print('4   ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '   6')
    print('    ---------')
    print('7   ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '   9')
    print('\n        8')
    print('Current selection {}:'.format(winner))

# Keep game running until winner
while playing:
    os.system('clear')
    print_game()
    if computer_turn:
        computer_move()
        player_go = True
    elif player_go:
        player_move()
        computer_turn = True
    winner = check_for_win()
    if winner == True:
        print_game()
        print('You Win')
        break
# Sleep then quit game
sleep(2)
playing = False