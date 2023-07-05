=============================
The ``100-matrix_mul`` module
=============================

Using ``matrix_mul``
---------------------   

Import the function:

    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul

Now test it:

correct Cases:
    >>> matrix_mul([[2, 4], [6, 8]], [[2, 4], [6, 8]])
    [[28, 40], [60, 88]]

    >>> matrix_mul([[6, 9]], [[1, 22], [14, 63]])
    [[132, 699]]

    >>> matrix_mul([[1, 2], [3, 4], [3, 4]],  [[5, 6, 1], [7, 8, 2]])
    [[19, 22, 5], [43, 50, 11], [43, 50, 11]]

Error Cases:
    >>> matrix_mul("[]", [[], []])
    Traceback (most recent call last):
    TypeError: m_a must be a list

    >>> matrix_mul([[], []], "[]")
    Traceback (most recent call last):
    TypeError: m_b must be a list

    >>> matrix_mul(["a", "b"], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

    Test for second argument not being a list of lists
    >>> matrix_mul([[1, 2], [3, 4]], ["a", "b"])
    Traceback (most recent call last):
    TypeError: m_b must be a list of lists

    >>> matrix_mul([["1", 2], [3, 4]], [[5, 6], [7, 8]])
    Traceback (most recent call last):
    TypeError: m_a should contain only integers or floats

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, "8"]])
    Traceback (most recent call last):
    TypeError: m_b should contain only integers or floats

    >>> matrix_mul([[1, 2], [3, 4]], [[], []])
    Traceback (most recent call last):
    ValueError: m_b can't be empty

    >>> matrix_mul([], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ValueError: m_a can't be empty

    >>> matrix_mul([[1, 2], [3, 4, 9]], [[5, 6], [7, 8]])
    Traceback (most recent call last):
    TypeError: each row of m_a must be of the same size

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8, 9]])
    Traceback (most recent call last):
    TypeError: each row of m_b must be of the same size

    >>> matrix_mul([[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

    >>> matrix_mul()
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'


    >>> matrix_mul([[1, 2, 3], [3, 4, 5]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ValueError: m_a and m_b can't be multiplied
