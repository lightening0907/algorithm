import pdb

def count_paths(dims, start, target, K):
    """
    @param dims, a tuple (width, height) of the dimensions of the board
    @param start, a tuple (x, y) of the king's starting coordinate
    @param target, a tuple (x, y) of the king's destination

    [url]@return[/url] the number of distinct paths there are for
    a king in chess (can move one square vertically, horizontally, or diagonally)
    to move from the start to target coordinates on the given board in K moves
    """
    location_candidate = {start:1}
    for step in range(K):
        location_candidate_temp = {}
        for location in location_candidate:
            for hor_mov in [-1, 0, 1]:
                for ver_mov in [-1, 0, 1]:
                    if not (hor_mov==0 and ver_mov==0):
                        location_new = location[0] + hor_mov, location[1] + ver_mov
                        if (0 <= location_new[0]< dims[0]) \
                            and (0 <= location_new[1] < dims[1]):
                            if location_new not in location_candidate_temp:
                                location_candidate_temp[location_new] = location_candidate[location]
                            else:
                                location_candidate_temp[location_new] += location_candidate[location]
        location_candidate = location_candidate_temp
    return location_candidate.get(target, 0)





if __name__ == "__main__":
    print "Running tests..."
    assert(count_paths((3, 3), (0, 0), (2, 2), 2) == 1)
    print "Passed test 1"
    assert(count_paths((3, 3), (0, 0), (2, 2), 3) == 6)
    print "Passed test 2"
    assert(count_paths((4, 4), (3, 2), (3, 2), 3) == 12)
    print "Passed test 3"
    assert(count_paths((4, 4), (3, 2), (1, 1), 4) == 84)
    print "Passed test 4"
    assert(count_paths((4, 6), (0, 2), (3, 4), 12) == 122529792)
    print "Passed test 5"