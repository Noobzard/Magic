import openpyxl
from MageAndCards import *
def choose_card_on_board(player1,player2):
    print("On your creatures ?")
    resp = input("Y/N")
    if resp == "Y" or resp == 'y':
        n = 0
        for i in player1.board[1]:
            print(n, " : ", i.name)
            n += 1
        print("Choose a card")
        choice = int(input())
        return player1.board[1][choice]
    else:
        n = 0
        for i in player2.board[1]:
            print(n, " : ", i.name)
            n += 1
        print("Choose a card")
        choice = int(input())
        return player2.board[1][choice]