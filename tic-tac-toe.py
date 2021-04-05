import random
import os
from time import sleep

playing = True
computer_turn = True
computer_wins = 0
player_wins = 0
board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

def reset_game():
    global computer_turn
    computer_turn = True
    board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

# Check to see if there are 3 x's or o's in a row
def check_for_win():
    global player_wins
    global computer_wins
    wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    for x,y in board.items():
        if y == 'X' or y == 'O':
            for i in wins:
                if x not in i:
                    pass
                else:
                    i.append(y)
                    i.remove(x)
    for b in wins:
        if b == ['X','X','X']:
            playing_game = False
            player_wins += 1
            break
        elif b == ['O','O','O']:
            playing_game = False
            computer_wins +=1
            break
        else:
            playing_game = True
            break
    return playing_game


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
    print('Player wins: {}'.format(player_wins))

# Keep game running until winner
def playing():
    computer_move()
    player_move()
    winner = check_for_win()
    if not winner:
        print('You win')
    print_game()

playing()

# Sleep then quit game
print_game()
sleep(2)
reset_game()
