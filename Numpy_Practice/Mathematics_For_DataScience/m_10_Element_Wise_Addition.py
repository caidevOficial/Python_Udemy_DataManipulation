# MIT License

# Copyright (c) 2022 [FacuFalcone]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
from m_00_Common_Variables import *

def element_wise_addition(matrix_1: np.ndarray, matrix_2: np.ndarray) -> np.ndarray:
    """[summary]\n
    Adds two matrices element-wise. Both shapes MUST be same size.

    Arguments:
        matrix_1 {np.ndarray} -- First matrix to be added
        matrix_2 {np.ndarray} -- Second matrix to be added

    Returns:
        np.ndarray -- Matrix with the element-wise addition 
    """
    if matrix_1.shape != matrix_2.shape:
        raise ValueError("The matrices must have the same shape.")
    return matrix_1 + matrix_2

if __name__ == "__main__":
    # ?#### Creates a Matrix to be used in the next snippet
    the_matrix_1 = CreateMatrixArray(BASIC_ARRAY_1, BASIC_ARRAY_2)
    the_matrix_2 = CreateMatrixArray(BASIC_ARRAY_2, BASIC_ARRAY_1)

    # ?#### Prints the matrix
    print(f'Matrix 1: \n{the_matrix_1}')
    print(f'Matrix 2: \n{the_matrix_2}')

    # ?#### Adds each element of the matrix to the same element of the other matrix
    element_wise_addition_matrix = element_wise_addition(the_matrix_1, the_matrix_2)

    # ?#### Prints the matrix [element-wise addition]
    print(f'Element-wise addition: \n{element_wise_addition_matrix}')
