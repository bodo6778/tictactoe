import os


def clear():
    os.system('cls')


testBoard = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
global board
board = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player1 = ''
player2 = ''

def display_game_board(board):
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print("-----------")
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print("-----------")
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')


def start_game():
    print("Welcome to TicTacToe! Let's choose sides.")
    global player1
    global player2
    global board
    board = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    characterChosen = 0
    while characterChosen == 0:
        player1 = input("Player 1, type X or 0 to choose your player: ")
        player1 = player1.upper()
        if player1 == 'X':
            player2 = '0'
            characterChosen = 1
        elif player1 == '0':
            player2 = 'X'
            characterChosen = 1
        else:
            print("You did not choose the right characters! Let's try again.")
    print("Good, you will go first and player 2 will be " + player2)
    ready_to_play()


def ready_to_play():
    ready = input("Are you ready to play? (Y/N) ")
    ready = ready.lower()
    if ready == 'y':
        clear()
        game_update()
    elif ready == 'n':
        print("See you soon!")
        return 0
    else:
        ready_to_play()


def game_update():
    end = False
    turn = 0
    while end is False:
        clear()
        display_game_board(board)
        if turn % 2 == 0:
            currentPlayer = player1
            player_input(currentPlayer)
        else:
            currentPlayer = player2
            player_input(currentPlayer)
        turn = turn + 1
        if board == testBoard:
            print("---------------------------------------------")
            print("TIE!")
            print("---------------------------------------------")
            break
        if check_win(board,currentPlayer) == 1:
            display_game_board(board)
            print("---------------------------------------------")
            print(currentPlayer + " wins!")
            print("---------------------------------------------")
            break
    ready = input("Do you want to play again? (Y/N) ")
    ready = ready.lower()
    if ready == 'y':
        clear()
        start_game()
    else:
        ready == 'n'
        print("See you soon!")
        return 0


def player_input(player):
    position = input(f"{player} will be placed at position: ")
    while len(position) != 1 or ord(position) > ord('9'):
        position = input("You did not enter a valid digit. Try again: ")
    while len(position) != 1 or ord(position) < ord('1'):
        position = input("You did not enter a valid digit. Try again: ")
    while True:
        if board[int(position)] == ' ':
            break
        else:
            position = input("Your position is already occupied. Try again: ")
    board[int(position)] = player
    print("PLAYER:  " + player)


def check_win(board, player):
    for i in range(0,3):
        if board[i*3+1] == board[i*3+2] and board[i*3+2] == board[i*3+3] and board[i*3+1] == player:
            print("1")
            return 1

        if board[1+i] == board[4+i] and board[4+i] == board[7+i] and board[1+i] == player:
            print("2")
            return 1

    if board[1] == board[5] and board[5] == board[9] and board[1] == player:
        print("3")
        return 1
    if board[3] == board[5] and board[5] == board[7] and board[3] == player:
        print("4")
        return 1

    return 0


start_game()


