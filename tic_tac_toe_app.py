import pygame
from tic_tac_toe_game import TicTacToe
from time import sleep



# Initialize pygame
pygame.init()

# Set up display
WINDOW_SIZE = 450  # Artırılan boyut
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
        pygame.draw.line(WINDOW, BLACK, (i * 150, 0), (i * 150, WINDOW_SIZE), 7)  # Artırılan boyuta uygun olarak güncellendi
        pygame.draw.line(WINDOW, BLACK, (0, i * 150), (WINDOW_SIZE, i * 150), 7)  # Artırılan boyuta uygun olarak güncellendi

    # Draw X's and O's
    for i in range(3):
        for j in range(3):
            if current_board[i][j] == 'X':
                pygame.draw.line(WINDOW, BLACK, (j * 150 + 30, i * 150 + 30), (j * 150 + 120, i * 150 + 120), 7)  # Artırılan boyuta uygun olarak güncellendi
                pygame.draw.line(WINDOW, BLACK, (j * 150 + 30, i * 150 + 120), (j * 150 + 120, i * 150 + 30), 7)  # Artırılan boyuta uygun olarak güncellendi
            elif current_board[i][j] == 'O':
                pygame.draw.circle(WINDOW, BLACK, (j * 150 + 75, i * 150 + 75), 50, 7)  # Artırılan boyuta uygun olarak güncellendi

# Function to handle player's move
def handle_move(row, col):
    if current_board[row][col] == ' ':
        current_board[row][col] = 'O'
        return True
    return False

# Main game loop
while not game.terminal(current_board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // 150, x // 150
            if handle_move(row, col):
                action = (row + 1, col + 1)
                current_board = game.result(current_board, action)

                # Check if the game is still not over
                if not game.terminal(current_board):
                    # Let AI make a move
                    ai_action = game.minimax(current_board)
                    if ai_action:
                        current_board = game.result(current_board, ai_action)

    draw_board()
    pygame.display.update()

# Determine winner
winner = game.winner(current_board)
if winner:
    print(f'{winner} wins!')
    sleep(1.5)
else:
    print("It's a draw!")
    sleep(1.5)

# Quit pygame
pygame.quit()
