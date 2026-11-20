## CONSTANTS
# Define board size
BOARD_SIZE = 5
# Define markers and who moves next
EMPTY = "-"
X = "X"
O = "O"
def won_game(board: list[list[str]], marker: str) -> bool:
    """Determines if a marker has won the game.
        Args:
            board (list[list[str]]): current board state.
            marker (str): marker to test for win.
        Returns:
            bool: True if this marker has achieved a win state, False otherwise.
    """
    if won_rows(board, marker) or won_columns(board, marker) or won_diagonal(board, marker):
        return True
    else:
        return False

def won_rows(board: list[list[str]], marker: str) -> bool:
    """Determines if a marker has won the game by filling a row.
    Args:
    board (list[list[str]]): current board state.
    marker (str): marker to test for win.
    Returns:
    bool: True if this marker has filled one of the rows, False otherwise.
    """
    for i in range(BOARD_SIZE):
        if board[i] == [marker]*BOARD_SIZE:
            return True
    return False


def won_columns(board: list[list[str]], marker: str) -> bool:
    """Determines if a marker has won the game by filling a column.
    Args:
    board (list[list[str]]): current board state.
    marker (str): marker to test for win.
    Returns:
    bool: True if this marker has filled one of the columns, False otherwise.
    """
    for i in range(BOARD_SIZE):
        count = 0
        for a in range(len(board)):
            if board[a][i] == marker:
                count += 1
        if count == BOARD_SIZE:
            return True
    return False
            

def won_diagonal(board: list[list[str]], marker: str) -> bool:
    """Determines if a marker has won the game by filling a diagonal.
    Args:
    board (list[list[str]]): current board state.
    marker (str): marker to test for win.
    Returns:
    bool: True if this marker has filled one of the diagonals, False otherwise.
    """
    i = 0
    e = 0
    for a in range(len(board)):
        if board[a][a] == marker:
            i += 1
        if board[BOARD_SIZE-1-a][a] == marker:
            e += 1
    if i == BOARD_SIZE or e == BOARD_SIZE:
        return True
    else:
        return False

            

def filled(board: list[list[str]]) -> bool:
    """Determines if a tic-tac-toe board is filled with symbols.
    Args:
    board (list[list[str]]): current board state.
    Returns:
    bool: if the game board has no moves remaining.
    """
    for a in range(len(board)):
        for b in range(len(board[a])):
            if board[a][b] == EMPTY:
                return False
    return True

def print_board(board: list[list[str]]) -> None:
    """Prints the current board state to the console.
    Args:
    board (list[list[str]]): current board state
    """
    for row in range(BOARD_SIZE):
        print(row + 1, *board[row], sep="")
    
    print(" ", *range(1, BOARD_SIZE + 1), sep="")

def main():
    # X moves first
    to_move = X
    
    # Fill board - extra fancy!
    board = []
    for row in range(BOARD_SIZE):
        board.append([EMPTY] * BOARD_SIZE)
    
    # Run turns of game
    while not filled(board):
    # Print current board state
        print_board(board)
        
        print(to_move + "'s move")

        # Take next move
        row, col = map(int, input("Enter move in the form row col ").split())
        board[row - 1][col -1] = to_move

        # See if this won the game
        if won_game(board, to_move):
            print("You win!")
            break

        # Change whose move is
        if to_move == X:
            to_move = O
        else:
            to_move = X
main()