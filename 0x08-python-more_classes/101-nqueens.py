#!/usr/bin/python3
"""Program to compute solutions to the 'N Queens' problem.

The 'N Queens' problem is to enumerate all the possible arrangements
of N Queens on an NxN chessboard such that no two pieces lie along
the same vertical, horizontal, or diagonal. It is difficult to compute
by brute force because even for relatively small `n` the number of
arrangements to test grows factorially (N**2 choose N). The solution
uses backtracking to quickly prune the tree of possible arrangments by
abandoning unsuccessful branches once a partial solution can be rejected.

Example:
    This program can be invoked from the command line by specifying the
    value for `n`, such as:

        $ ./nqueens 8
"""


def nqueens(n, c=[]):
    """Routine to recursively compute solutions to N queens problem.

    Recursively computes solutions until all branches of solution
    tree have been visited. Partial solutions that can be rejected
    are skipped over.

    Args:
        n (int): dimensions of board and number of queens.
        c (list): list of current candidate positions for solution.

    Output: Prints valid solutions to stdout.
    """
    if reject(n, c):
        return
    if accept(n, c):
        print(c)
    s = first_candidate(n, c)
    while s is not None:
        nqueens(n, s)
        s = next_candidate(n, s)


def reject(n, c):
    """Subroutine to test whether current partial solution is valid.

    Tests whether the most recently added position is in conflict
    with any other positions. Earlier positions are assumed to be
    valid as they were previously tested against those in the list
    before them.

    Args:
        n (int): dimensions of board and number of queens.
        c (list): list of current candidate positions for solution.

    Returns: True if the final position is in conflict with an earlier
        position, otherwise False.
    """
    try:
        last = c[-1]
    except IndexError:
        return False
    for i in c[:-1]:
        if i[0] == last[0] or i[1] == last[1]:
            return True
        if abs(last[0] - i[0]) == abs(last[1] - i[1]):
            return True
    return False


def accept(n, c):
    """Subroutine to test whether current list of positions is a solution.

    If the current candidate solution has not been rejected and is of
    length `n`, then it can be assumed to be a valid solution.

    Args:
        n (int): dimensions of board and number of queens.
        c (list): list of current candidate positions for solution.

    Returns: True if len(c) == n, otherwise False.
    """
    if len(c) == n:
        return True
    return False


def first_candidate(n, c):
    """Subroutine to add position to the end of the candidate solution.

    If the previous position was not rejected and the length of the
    `c` is less than `n`, this function adds the next candidate position
    following the last position.

    Args:
        n (int): dimensions of board and number of queens.
        c (list): list of current candidate positions for solution.

    Returns: New list with added position, or None if len(c) == n.
    """
    if len(c) == n:
        return None
    try:
        last = c[-1]
    except IndexError:
        return [[0, 0]]
    if last[1] < n-1:
        return c + [[last[0], last[1]+1]]
    elif last[0] < n-1:
        return c + [[last[0]+1, 0]]
    else:
        return None


def next_candidate(n, s):
    """Subroutine to update last position of candidate solution.

    If the previous solution was rejected, the final position is
    advanced to the next position, unless the end of the board
    has been reached, in which case this function returns None.

    Args:
        n (int): dimensions of board and number of queens.
        s (list): list of current candidate positions for solution.

    Returns: New list of candidate positions for solution, or None if
        at end of board.
    """
    last = s[-1]
    if last[1] < n-1:
        return s[:-1] + [[last[0], last[1]+1]]
    elif last[0] < n-1:
        return s[:-1] + [[last[0]+1, 0]]
    else:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print('N must be a number')
        exit(1)
    n = int(n)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    nqueens(n)
    exit(0)
