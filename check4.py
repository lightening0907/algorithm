import numpy as np


def check_equivalence(board, new_location_x, new_location_y,
                      old_location_x, old_location_y, start_locations, skip_location):
    if (new_location_x, new_location_y) not in skip_location \
            and (new_location_x, new_location_y) not in start_locations:
            start_locations[(new_location_x, new_location_y)] = True
    if (board[new_location_x, new_location_y] != board[old_location_x, old_location_y]) \
            or board[old_location_x, old_location_y] == 0:

        return False
    return True


def check_horiz(location, board, width, start_locations, skip_location):
    location_x, location_y = location
    for new_location_y in range(location_y + 1, location_y + 4):
        if not (new_location_y < width):
            return False
        if not check_equivalence(board, location_x, new_location_y, location_x, location_y, start_locations,
                                 skip_location):
            return False

    return True


def check_vert(location, board, height, start_locations, skip_location):
    location_x, location_y = location
    for new_location_x in range(location_x + 1, location_x + 4):

        if not (new_location_x < height):
            return False
        if not check_equivalence(board, new_location_x, location_y, location_x, location_y, start_locations,
                                 skip_location):
            return False
    return True


def check_diag_f(location, board, width, height, start_locations, skip_location):
    location_x, location_y = location
    for inc in range(1, 4):
        new_location_x = location_x + inc
        new_location_y = location_y + inc
        if not (new_location_x < height
                and new_location_y < width):
            return False

        if not check_equivalence(board, new_location_x, new_location_y, location_x, location_y, start_locations,
                                 skip_location):
            return False
    return True


def check_diag_b(location, board, height, start_locations, skip_location):
    location_x, location_y = location
    for inc in range(1, 4):
        new_location_x = location_x + inc
        new_location_y = location_y - inc
        if not (new_location_x < height
                and new_location_y >= 0):
            return False
        if not check_equivalence(board, new_location_x, new_location_y, location_x, location_y, start_locations,
                                 skip_location):
            return False
    return True


def check4(board):
    """
    Args:
     board: numpy array of 0, 1, 2 where 1 belongs to player 1,
      2 belongs to player 2 and 0 is empty
    Return:
     result: 1 if player 1 wins, 2 if player 2 wins, and 0 if no one wins
    """
    start_locations = {(0, 0): True}  # init location to check for the win
    # location where we know for sure that couldn't belong to 4 in a row for play 1, 2 or 0 (both)
    skip_location = {}
    height, width = board.shape
    while len(start_locations) > 0:
        start_location, _ = start_locations.popitem()
        flag = False
        flag = flag | check_horiz(start_location, board, width, start_locations, skip_location)
        flag = flag | check_vert(start_location, board, height, start_locations, skip_location)
        flag = flag | check_diag_f(start_location, board, width, height, start_locations, skip_location)
        flag = flag | check_diag_b(start_location, board, height, start_locations, skip_location)
        if flag:
            return board[start_location[0], start_location[1]]
        else:
            skip_location[(start_location[0], start_location[1])] = board[start_location[0], start_location[1]]

    return 0

board = np.array([[0, 0, 0, 0, 0, 0],
                  [1, 2, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0],
                  [0, 2, 1, 0, 0, 0],
                  [0, 2, 0, 1, 0, 0]
                  ])


board2 = np.array([[0, 0, 0, 0, 0, 0],
                  [1, 2, 0, 0, 0, 0],
                  [0, 2, 0, 0, 0, 0],
                  [0, 2, 1, 0, 0, 0],
                  [0, 2, 0, 1, 0, 0]
                  ])

board3 = np.array([[2, 2, 0, 0, 0, 0],
                  [1, 2, 2, 2, 2, 0],
                  [0, 1, 0, 1, 0, 0],
                  [0, 2, 1, 0, 0, 0],
                  [2, 2, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0]
                  ])

board4 = np.array([[2, 2, 1, 1],
                  [2, 2, 2, 2],
                  [1, 0, 1, 0],
                  [1, 0, 0, 1]])

print "the winner is:", check4(board)

# check for solution https://stackoverflow.com/questions/29949169/python-connect-4-check-win-function