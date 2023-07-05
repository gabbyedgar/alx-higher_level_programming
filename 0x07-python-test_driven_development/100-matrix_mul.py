#!/usr/bin/python3

"""
Module matrix_mul
matrix_mul

"""


def matrix_mul(m_a, m_b):
    """
    Multiply matrix
    """
    if type(m_a) != list:
        raise TypeError('m_a must be a list')
    if type(m_b) != list:
        raise TypeError('m_b must be a list')

    if not len(m_a):
        raise ValueError("m_a can't be empty")
    if not len(m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(item, list) for item in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError('m_b must be a list of lists')

    if any(not len(item) for item in m_a):
        raise ValueError("m_a can't be empty")
    if any(not len(item) for item in m_b):
        raise ValueError("m_b can't be empty")

    for r in m_a:
        if not all(isinstance(n, (int, float)) for n in r):
            raise TypeError('m_a should contain only integers or floats')
    for r in m_b:
        if not all(isinstance(n, (int, float)) for n in r):
            raise TypeError('m_b should contain only integers or floats')

    lr = list(map(lambda i: len(i), [i for i in m_a]))

    if lr.count(lr[0]) != len(lr):
        raise TypeError('each row of m_a must be of the same size')

    lr = list(map(lambda i: len(i), [i for i in m_b]))
    if lr.count(lr[0]) != len(lr):
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(a_r, b_c))
               for b_c in zip(*m_b)]
              for a_r in m_a]
    return result
