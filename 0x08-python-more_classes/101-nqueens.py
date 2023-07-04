#!/usr/bin/python3
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

    if len(c) == n:
        return True
    return False


def first_candidate(n, c):

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

    last = s[-1]
    if last1] < n-1:
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
