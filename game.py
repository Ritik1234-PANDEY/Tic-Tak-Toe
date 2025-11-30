# Tic Tac Toe game in Python (2 Player - Console Version)

def print_board(board):
    """Board ko screen par print karta hai."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    """Check karta hai ki given player jeeta hai ya nahi."""
    winning_combinations = [
        (0, 1, 2),  # row 1
        (3, 4, 5),  # row 2
        (6, 7, 8),  # row 3
        (0, 3, 6),  # column 1
        (1, 4, 7),  # column 2
        (2, 5, 8),  # column 3
        (0, 4, 8),  # diagonal
        (2, 4, 6)   # diagonal
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    """Agar saare cells fill ho gaye aur koi winner nahi hai to draw."""
    return all(cell != " " for cell in board)


def get_valid_move(board):
    """User se valid move (1-9) leta hai."""
    while True:
        move = input("Choose a position (1-9): ")
        if not move.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        move = int(move)
        if move < 1 or move > 9:
            print("Invalid position! 1 se 9 ke beech ka number dalo.")
            continue

        index = move - 1
        if board[index] != " ":
            print("Ye position already filled hai, koi aur position choose karo.")
            continue

        return index


def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player X and Player O turn by turn khelenge.")
    print("Positions is tarah se hain:\n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    # Empty board banate hain
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player} ki baari hai.")
        move_index = get_valid_move(board)
        board[move_index] = current_player

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("Match Draw! 😅")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if "_name_" == "_main_":
    while True:
        play_game()
        again = input("Kya aap dobara khelna chahenge? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for playing! Bye 👋")
            break