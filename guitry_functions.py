

def clear_board(board): # clear the board for a new game
    for key in board.keys():
        board[key]=key


def is_win_scores(board, turn, sp1, sp2,status_text, status_color, apply_score=True):


    # player 1 wins
    p1 = (
        (board["1"] == "x" and board["2"] == "x" and board["3"] == "x") or
        (board["4"] == "x" and board["5"] == "x" and board["6"] == "x") or
        (board["7"] == "x" and board["8"] == "x" and board["9"] == "x") or
        (board["1"] == "x" and board["4"] == "x" and board["7"] == "x") or
        (board["2"] == "x" and board["5"] == "x" and board["8"] == "x") or
        (board["3"] == "x" and board["6"] == "x" and board["9"] == "x") or
        (board["1"] == "x" and board["5"] == "x" and board["9"] == "x") or
        (board["3"] == "x" and board["5"] == "x" and board["7"] == "x")
    )
    if p1:
        if apply_score:
            status_text="player 1 win!"
            sp1 += 1
            status_color=(0,255,0)
        return (True, sp1, sp2,status_text,status_color)

    # player 2 wins
    p2 = (
        (board["1"] == "o" and board["2"] == "o" and board["3"] == "o") or
        (board["4"] == "o" and board["5"] == "o" and board["6"] == "o") or
        (board["7"] == "o" and board["8"] == "o" and board["9"] == "o") or
        (board["1"] == "o" and board["4"] == "o" and board["7"] == "o") or
        (board["2"] == "o" and board["5"] == "o" and board["8"] == "o") or
        (board["3"] == "o" and board["6"] == "o" and board["9"] == "o") or
        (board["1"] == "o" and board["5"] == "o" and board["9"] == "o") or
        (board["3"] == "o" and board["5"] == "o" and board["7"] == "o")
    )
    if p2:
        if apply_score:
            status_text="player 2 win!"
            sp2 += 1
            status_color=(0,0,255)
        return (True, sp1, sp2,status_text,status_color)
     
        # Tie
    if turn == 10:
        if apply_score:
            status_text="it's a tie"
            status_color=(128,128,128)
        return (True, sp1, sp2,status_text,status_color)

    return (False, sp1, sp2,status_text,status_color)


def is_win(board,turn):
    # Backwards-compatible boolean wrapper used by other code (like smartAI)
    return is_win_scores(board, turn, 0,0, status_text="", status_color=(0,0,0), apply_score=False)


def smartAI(board, turn, sp1=0, sp2=0):

    # Check if AI can win (top priority) -- simulate without applying score or printing
    for key in board.keys():
        if board[key] == key:
            board[key] = "o"
            if is_win(board, turn)[0]:
                return board
            board[key] = key
    
    # Check if need to defend (high priority)
    for key in board.keys():
        if board[key] == key:
            board[key] = "x"
            # if opponent would win here, block
            if is_win(board, turn)[0]:
                board[key] = "o"
                return board
            board[key] = key
    
            # Check center
    if board["5"] == "5":
        board["5"] = "o"
        return board
    
    # Check corners
    for x in ("1", "3", "7", "9"):
        if board[x] == x:
            board[x] = "o"
            return board
    
    # Check remaining positions
    for x in ("2", "4", "6", "8"):
        if board[x] == x:
            board[x] = "o"
            return board
    



