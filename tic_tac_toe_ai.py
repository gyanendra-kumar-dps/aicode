<<<<<<< HEAD
=======
from colorama import Fore,init
import random
init(autoreset=True)
board=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
def print_board():
    board1=f'{board[0][0]} | {board[0][1]} | {board[0][2]}\n'
    sep1='---------\n'
    board2=f'{board[1][0]} | {board[1][1]} | {board[1][2]}\n'
    sep2='---------\n'
    board3=f'{board[2][0]} | {board[2][1]} | {board[2][2]}'
    return board1+sep1+board2+sep2+board3
def choice():
    chce=input(f"{Fore.BLUE}What's your choice X/O:")
    if chce.upper()=='X':
        return chce.upper()
    elif chce.upper()=='O':
        return chce.upper()
    else:
        print(f'{Fore.RED}Please enter only X/O')
        choice()
def player_turn(choice):
    col=input(f'{Fore.BLUE}Enter coulumn:')
    row=input(f'{Fore.BLUE}Enter row:')
    if col.isdigit() and len(col)==1 and int(col)<=3 and row.isdigit() and len(row)==1 and int(row)<=3:
        print(f'{Fore.GREEN}valid statement')
        board[int(col)][int(row)]=choice
        print(print_board())
        return [col,row]
    else:
        player_turn()
def bot_turn(board):
    choice_col=[]
    choice_row=[]
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j]=='X' or board[i][j]=='O':
                pass
            else:
                choice_col.append(i)
                choice_row.append(j)
    print(random.choices(choice_col))
    print(random.choices(choice_row))
abc=choice()
print(player_turn(abc))
print(bot_turn(board))
>>>>>>> 5603fce (first commit)
