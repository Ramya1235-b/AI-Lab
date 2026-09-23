# Tic-Tac-Toe Game

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

player = "X"

while True:
    print("\n-------------------")
    print("    TIC TAC TOE")
    print("-------------------")

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

    print("\nPlayer", player, "turn")

    position = int(input("Enter a position (1-9): ")) - 1

    if board[position] == " ":
        board[position] = player
    else:
        print("That position is already taken!")
        continue

    # Check if the player has won
    if (
        board[0] == board[1] == board[2] != " " or
        board[3] == board[4] == board[5] != " " or
        board[6] == board[7] == board[8] != " " or
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
        board[2] == board[4] == board[6] != " "
    ):
        print("\nPlayer", player, "wins!")
        break

    # Check for a draw
    if " " not in board:
        print("\nIt's a draw!")
        break

    # Change player
    if player == "X":
        player = "O"
    else:
        player = "X"

print("\nGame Over!")
