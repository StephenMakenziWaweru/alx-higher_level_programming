#!/usr/bin/python3
"""Module for lazy_matrix_mul method."""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies one matrix by another.
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the product
    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    '''
    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    m_a_scalar = False
    m_b_scalar = False
    for row in m_a:
        if not isinstance(row, list):
            m_a_scalar = True
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            m_b_scalar = True
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True

    '''
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0)x:
        raise ValueError("m_b can't be empty")
    '''

    if m_a_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_b_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_a_notnum:
        raise TypeError("invalid data type for einsum")

    if m_b_notnum:
        raise TypeError("invalid data type for einsum")

    if m_a_notrect:
        raise ValueError("setting an array element with a sequence.")

    if m_b_notrect:
        raise ValueError("setting an array element with a sequence.")

    '''
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            res[i].append(c)
    '''
    return numpy.matrix(m_a) * numpy.matrix(m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
