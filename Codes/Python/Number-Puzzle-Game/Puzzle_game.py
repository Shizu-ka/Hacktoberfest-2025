import random

# Function to display the board
def display(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

# Function to find the position of 0 (empty space)
def find_empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

# Function to check if the puzzle is solved
def is_solved(board):
    target = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]
    return board == target

# Function to make a move
def move(board, direction):
    i, j = find_empty(board)
    if direction == 'up' and i < 2:
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    elif direction == 'down' and i > 0:
        board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
    elif direction == 'left' and j < 2:
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
    elif direction == 'right' and j > 0:
        board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
    else:
        print("❌ Invalid move!")

# Function to shuffle the board
def shuffle_board(board):
    moves = ['up', 'down', 'left', 'right']
    for _ in range(50):
        move(board, random.choice(moves))

# Main Game
def puzzle_game():
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]

    shuffle_board(board)
    print("🧩 Welcome to the Number Puzzle Game!")
    print("Arrange the numbers from 1 to 8. Use commands: up, down, left, right\n")

    while True:
        display(board)
        if is_solved(board):
            print("🎉 Congratulations! You solved the puzzle!")
            break

        move_input = input("Move (up/down/left/right or 'quit'): ").lower()
        if move_input == "quit":
            print("👋 Thanks for playing!")
            break
        move(board, move_input)

# Run the game
if __name__ == "__main__":
    puzzle_game()
