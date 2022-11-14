print("""
/////////////////////////////////////////////////////////////////////////////////////////////
          THE GAME NIM RULES

    the program assumes that the inputs are ints, for example, if you are asked to choose a row number 
    you cant choose 1.3 / "row Two"/ "  "  becase there is no such row.

    the program assumes that the inputs are ints, for example, if you are asked to choose how many sticks to remove 
    you cant choose 1.3.

    you cant skip your turn becase it against the rules of the game, and you cant remove zero sticks

    there is a tiny possibility the board that will be generated will have only one row with one stick, then the first player will lose.

    the game will end when there will bw o sticks left, whitch means the player who playes last is the loser

    GOOD LUCK :)
    
////////////////////////////////////////////////////////////////////////////////////////////

""")

import random

board_list =[]
MAX_ROWS = 10 
MAX_STICKS_IN_ROW = 10

def update_board():
    '''
    the main function that calles the other functions and updats the board depending on the input of the players, untill the board is empty
    '''
    init_board() 
    print_board()
    print("lets start :) \n FIRST PLAYER'S TURN")
    first_player_turn = True
    while is_board_empty()==False:
        row_removed_from, amount_taken = get_input()
        if check_row_number_validity(row_removed_from):#checks if the row input is correct
            if check_amount_taken(row_removed_from,amount_taken): #if all the input is correct update the board accordint to the input
                board_list[int(row_removed_from)-1] = int(board_list[int(row_removed_from)-1]) - int(amount_taken)
                print_board() # prints the updated board
                first_player_turn =  get_next_player(first_player_turn) #changes the turn to be the other's player 

            else :
                print("OH NO! wrong input: Tthe sticks amount in this row is too low")
        else:
            print ("OH NO! wrong input: this row is not available")
    print( "  ","*"*11 , "\n GAME OVER" , "\n" , "*"*11)
    if(first_player_turn==True):
        print("THE WINNER IS THE FIRST PLAYER !")
    else:
        print("THE WINNER IS THE SECOND PLAYER !")


def init_board():
    '''
    a function that generates a random number of rows (smaller than 10) and in each row it puts a random number of sticks (smaller than 10)
    '''
    rows_number = int((random.random())*10)
    while (rows_number < MAX_ROWS/10): # the number of rows must be bigger than one
        rows_number = int((random.random())*10)
    for i in range(1,rows_number):
        sticks_number = int((random.random())*10)
        while (sticks_number< MAX_STICKS_IN_ROW/10): # the number of rows must be bigger than one
            sticks_number = int((random.random())*10)
        board_list.append(sticks_number)
    return board_list


def print_board():
    '''
    prints the board according to the board list.
    '''
    for i in range(0,len(board_list)):
        print("|" * board_list [i] ," "*(10-board_list[i]),  board_list [i],  " - sticks left in this row")


def get_input():
    '''
    this function gets input from the players and returns it
    '''
    reduse_row_num_input = input("choose row number")
    reduse_amout_input = input("how many sticks would you like to remove?")
    return reduse_row_num_input,reduse_amout_input


def check_row_number_validity(rows_number_input):
    '''
    this function checks the input of the row number, 
    it has to be bigger than zero and smaller than the total amount of rows,
    if the input correct it returns true, else, it returns false
    '''
    if int(rows_number_input) <= len(board_list) and int(rows_number_input) > 0:
        return True
    return False


def check_amount_taken(row_removed_from,amount_taken):
    '''
    this function checks the input of the amount of sticks that the player wants to remove,
     it has to be bigger than zero and smaller or even to the amount of sticks in this row,
    if the input correct it returns true, else, it returns false
    '''
    sticks_left_in_row = board_list[int(row_removed_from)-1]
    if int(amount_taken) <= int(sticks_left_in_row )and int(amount_taken) >0 :
        return True
    return False


def get_next_player(first_player_turn):
    '''
    the function gets the variable "first_player_turn" 
    and changes the boolean variable "firstPlayersturn" to false if it was true and to true is it was false
    '''
    if  first_player_turn == True: #if it was seconds players turn now it wont be
        first_player_turn = False
        print("SECOND PLAYER'S TURN")
    else: #if it wast seconds players turn now it will be
        first_player_turn = True
        print("FIRST PLAYER'S TURN")
    return first_player_turn


def is_board_empty():
    '''
    checks if the board is empty, if al the rows have zero sticks,
    returns true if it is empty
    '''
    allEmpty = True
    for i in range(0, len(board_list)):
        if int(board_list[i]) != 0 :
            allEmpty = False
    return allEmpty



update_board()