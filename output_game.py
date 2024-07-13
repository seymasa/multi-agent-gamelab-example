import random

# Constants
HEIGHT = 3
WIDTH = 5
PRINCESS = "P"
PRINCE = "R"
MONSTER = "M"
EMPTY = " "
GOAL = "G"


def create_game_board(height, width, num_monsters):
    board = [[EMPTY for _ in range(width)] for _ in range(height)]

    # Place the princess at the start (top-left)
    board[0][0] = PRINCESS

    # Place the goal at the end (bottom-right)
    board[height - 1][width - 1] = GOAL

    # Place monsters randomly
    for _ in range(num_monsters):
        while True:
            x = random.randint(0, height - 1)
            y = random.randint(0, width - 1)
            if board[x][y] == EMPTY:
                board[x][y] = MONSTER
                break

    return board


def print_board(board):
    for row in board:
        print("".join(row))


def move_princess(board, direction):
    height = len(board)
    width = len(board[0])

    # Find the princess
    princess_pos = None
    for i in range(height):
        for j in range(width):
            if board[i][j] == PRINCESS:
                princess_pos = (i, j)
                break
        if princess_pos:
            break

    if not princess_pos:
        return None

    # Calculate new position
    x, y = princess_pos
    if direction == "UP":
        new_pos = (max(0, x - 1), y)
    elif direction == "DOWN":
        new_pos = (min(height - 1, x + 1), y)
    elif direction == "LEFT":
        new_pos = (x, max(0, y - 1))
    elif direction == "RIGHT":
        new_pos = (x, min(width - 1, y + 1))
    else:
        new_pos = princess_pos

    # Check the new position
    nx, ny = new_pos
    if board[nx][ny] == MONSTER:
        return "GAME OVER"
    elif board[nx][ny] == GOAL:
        return "VICTORY"
    else:
        board[x][y] = EMPTY
        board[nx][ny] = PRINCESS
        return None


def main():
    num_monsters = int(input("Enter the number of monsters: "))

    board = create_game_board(HEIGHT, WIDTH, num_monsters)

    while True:
        print_board(board)

        direction = input("Enter direction (UP, DOWN, LEFT, RIGHT): ").upper()

        if direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            result = move_princess(board, direction)
        else:
            print("Invalid direction. Please enter UP, DOWN, LEFT, or RIGHT.")
            continue

        if result:
            print(result)
            break


if __name__ == "__main__":
    main()
