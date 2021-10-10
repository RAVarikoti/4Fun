#!/usr/bin/python3.6

import sys
import os
import matplotlib as plt
from IPython.display import clear_output
import random

"Hello"

#player1 = input("Please Pick a marker 'X' or 'O': ")
#print("You chose" player1)

def clrscr():
    '\n'*100
    return

def display_board(board):
    clrscr()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])
    return

#test_board = ['#','X','O','X','O','X','O','X','O','X']
#test_board = [' ']*10

#display_board(test_board)

def player_input():   

    marker = ' '
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    """player1 = marker
    if player1 == 'X':
        player2 == 'O'
    else:
        player2 == 'X'"""
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

    #print(player1, player2) 

#print(player_input())

def place_marker(board, marker, position):
    board[position] = marker
    pass

#place_marker(test_board,'R',8)
#display_board(test_board)


def win_check(board,mark):
    return ((board[7] == board[8] == board[9] == mark) or (board[4] == board[5] == board[6] == mark) or (board[1] == board[2] == board[3] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark))
        

#print(win_check(test_board,'X'))


def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
        
def space_check(board,position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose your position (1-9):  '))

    return position

def replay():
    choice = input ('Play again? Y or N: ')
    return choice == 'Y'

print ("Welcome to TIC Tac Toe")

while True:
    # play the game
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + 'will go first')

    play_game = input ('Ready to play? y or n ? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Game On

    while game_on:
        
        if turn == 'Player 1':
            display_board(the_board)  # show the board
            position = player_choice(the_board)      # choosing a position
            place_marker(the_board,player1_marker,position)    # placing marker on the position

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has Won!!!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)  # show the board
            position = player_choice(the_board)      # choosing a position
            place_marker(the_board,player2_marker,position)    # placing marker on the position

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has Won!!!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player 1'

    ### setting everything up(board, First, choose markers)
    if not replay():
        break

