import pygame
from tic_tac_toe_game import TicTacToe

# Initialize pygame
pygame.init()

# Set up display  
WINDOW_SIZE = 450
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize TicTacToe game
game = TicTacToe()
current_board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to draw the board
def draw_board():
    WINDOW.fill(WHITE)

    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(WINDOW, BLACK, (i * 150, 0), (i * 150, WINDOW_SIZE), 5)
        pygame.draw.line(WINDOW, BLACK, (0, i * 150), (WINDOW_SIZE, i * 150), 5)

    # Draw X's and O's
    for i in range(3):
        for j in range(3):
            if current_board[i][j] == 'X':
                pygame.draw.line(WINDOW, BLACK, (j * 150 + 30, i * 150 + 30), (j * 150 + 120, i * 150 + 120), 5)
                pygame.draw.line(WINDOW, BLACK, (j * 150 + 30, i * 150 + 120), (j * 150 + 120, i * 150 + 30), 5)
            elif current_board[i][j] == 'O':
                pygame.draw.circle(WINDOW, BLACK, (j * 150 + 75, i * 150 + 75), 50, 5)

# Function to handle player's move
def handle_move(row, col, player):
    if current_board[row][col] == ' ':
        current_board[row][col] = player
        return True
    return False

# Main game loop
current_player = 'X'
while not game.terminal(current_board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // 150, x // 150
            if handle_move(row, col, current_player):
                action = (row + 1, col + 1)
                current_board = game.result(current_board, action)

                # Switch player
                current_player = 'O' if current_player == 'X' else 'X'

    draw_board()
    pygame.display.update()

# Determine winner
winner = game.winner(current_board)
if winner:
    print(f'{winner} wins!')
else:
    print("It's a draw!")

# Quit pygame
pygame.quit()


