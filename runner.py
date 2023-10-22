

from time import sleep
from tic_tac_toe_game import TicTacToe


def print_board(board):                                 #create a board/tahta oluşturmak
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 9)

def main():                                             #running game fun./ oyunu oynama fonksiyonu
    game = TicTacToe()
    current_board = [[' ' for _ in range(3)] for _ in range(3)]

    while not game.terminal(current_board):
        print_board(current_board)
        sleep(1)
        if game.player(current_board) == 'X':
            print("X's turn")
            i, j = map(int, input("Enter row and column, example:('1 2'): ").split())
            action = (i, j)
            print("########################################################################################")
        else:
            print("O's turn")
            action = game.minimax(current_board)
            print("########################################################################################")

        current_board = game.result(current_board, action)

    print_board(current_board)
    winner = game.winner(current_board)
    if winner:                                  #winner and loser controlled/kazanan ve kaybeden kontrolu
        print(f'{winner} wins!')
    else:
        print("It's a draw!")

if __name__ == '__main__':
    main()
