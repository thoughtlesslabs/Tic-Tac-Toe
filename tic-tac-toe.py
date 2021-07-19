import random
import os
from time import sleep

board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
player_wins = 0

def menuoptions():
    startgame = input('Would you like to play a game? ')
    if startgame.lower() == 'yes' or startgame.lower() == 'y':
        resetgame()
        return True
    else:
        print('Thanks for Playing')
        exit()

def resetgame():
    global board
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
            return False,'Player',1
        elif b == ['O','O','O']:
            return False,'Computer',None
    return True, None, None

# Player gets to choose position, which must be empty
def player_move():
    player_go = True
    try:
        choice = int(input('Choose a location from 1 - 9: '))
    except ValueError:
        choice = int(input('Must be a number. Try again: '))
    while player_go:
        if choice == 10:
            exit()
        elif choice not in range(1,10):
            choice = int(input('Number must be between 1 and 9. Try again: '))
        elif board[choice] != ' ':
            choice = int(input('Pick a unoccupied spot: '))
        else:
            board.update({choice:'X'})
            player_go = False
    print_game()

# Automated computer move.
# Needs AI
def computer_move():
    computer_turn = True
    while computer_turn:
        pick_spot = random.randint(1,9)
        if board[pick_spot] != ' ':
            pick_spot = random.randint(1,9)
        else:
            board.update({pick_spot:'O'})
            computer_turn = False
    print_game()

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
    print('\nPlayer Wins: {}'.format(player_wins))

# Keep game running until winner
def playing():
    global player_wins
    print_game()
    while True:
        player_move()
        computer_move()
        winner = check_for_win()
        if winner[0]:
            continue
        else:
            break
    print('Congrats {}'.format(winner[1]))
    player_wins = player_wins + winner[2]
    print_game()
    keep_playing = menuoptions()
    if keep_playing:
        playing()

playing()

