# Function to initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in range(3):
        print('|'.join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print('-' * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

# Function to check if the board is full
def is_board_full(board):
    return all(space != ' ' for space in board)

# Main game logic
def play_game():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your position (1-9):")
        try:
            position = int(input()) - 1
            if board[position] != ' ' or position not in range(9):
                print("Invalid move. Try again.")
                continue
            board[position] = current_player

            # Check for a winner
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            # Check for a draw
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print("Please enter a valid number.")

# Run the game
play_game()