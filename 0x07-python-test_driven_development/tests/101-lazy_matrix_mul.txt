The ``101-lazy_lazy_matrix_mul`` module
============================

Using ``lazy_lazy_matrix_mul``
---------------------

Import module:
    >>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul
    
Test simply:
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    matrix([[19, 22],
            [43, 50]])

Test 2 bad matrices:
    >>> lazy_matrix_mul([[1, 2, 3], [3, 4, 5]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ...
    ValueError: shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)

Test 2 ok matrices:
    >>> lazy_matrix_mul([[1, 2], [3, 4], [3, 4]], [[5, 6, 1], [7, 8, 2]])
    matrix([[19, 22,  5],
            [43, 50, 11],
            [43, 50, 11]])

Test singly empty matrix:
    >>> lazy_matrix_mul([], [[3]])
    Traceback (most recent call last):
    ...  
    ValueError: shapes (1,0) and (1,1) not aligned: 0 (dim 1) != 1 (dim 0)

Test singly empty matrix:
    >>> lazy_matrix_mul([[]], [[3]])
    Traceback (most recent call last):
    ...
    ValueError: shapes (1,0) and (1,1) not aligned: 0 (dim 1) != 1 (dim 0)

Test singly empty matrix 2:
SHOULD BE ERROR
    >>> lazy_matrix_mul([[4]], [])
    matrix([], shape=(1, 0), dtype=float64)

Test doubly empty matrix:
SHOULD BE ERROR
    >>> lazy_matrix_mul([[3]], [[]])
    matrix([], shape=(1, 0), dtype=float64)

Test simple case:
    >>> lazy_matrix_mul([[3]], [[9]])
    matrix([[27]])

Test string arg:
    >>> lazy_matrix_mul("foo", [[9]])
    Traceback (most recent call last):
    ...
    TypeError: Scalar operands are not allowed, use '*' instead

Test string arg:
    >>> lazy_matrix_mul([[8]], "bar")
    Traceback (most recent call last):
    ...
    TypeError: Scalar operands are not allowed, use '*' instead

Test int list:
    >>> lazy_matrix_mul([1, 3, 4], [[9]])
    Traceback (most recent call last):
    ...
    TypeError: object of type 'int' has no len()

Test int list 2:
SHOULD BE ERROR
    >>> lazy_matrix_mul([[8]], [2, 4, 6])
    Traceback (most recent call last):
    ...
    TypeError: object of type 'int' has no len()


Test notnum list:
    >>> lazy_matrix_mul([["foo"]], [[2, 4, 6]])
    Traceback (most recent call last):
    ...
    TypeError: invalid data type for einsum

Test notnum list 2 :
    >>> lazy_matrix_mul([[2, 4, 6]], [["foo"]])
    Traceback (most recent call last):
    ...
    TypeError: invalid data type for einsum

Test a bad rows:
    >>> lazy_matrix_mul([[1, 2], [3, 4, 5], [3, 4]], [[5, 6, 1], [7, 8, 2]])
    Traceback (most recent call last):
    ...
    ValueError: setting an array element with a sequence.

Test b bad rows:
    >>> lazy_matrix_mul([[1, 2], [3, 4], [3, 4]], [[5, 6, 1], [7, 2]])
    Traceback (most recent call last):
    ...
    ValueError: setting an array element with a sequence.

Test missing 1 arg:
    >>> lazy_matrix_mul([[3]])
    Traceback (most recent call last):
    ...
    TypeError: lazy_matrix_mul() missing 1 required positional argument: 'm_b'

Test missing 2 args:
    >>> lazy_matrix_mul()
    Traceback (most recent call last):
    ...
    TypeError: lazy_matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

Test this
    >>> lazy_matrix_mul([[5, 6, 10], [7, 8]], [[5, 6], [7, 8]])
    Traceback (most recent call last):
    ...
    ValueError: setting an array element with a sequence.

String element:
    >>> lazy_matrix_mul([[5, '6'], [7, 8]], [[5, 6], [7, 8]])
    Traceback (most recent call last):
    ...
    TypeError: invalid data type for einsum


Test string arg:
    >>> lazy_matrix_mul("foo", [[9]])
    Traceback (most recent call last):
    ...
    TypeError: Scalar operands are not allowed, use '*' instead
