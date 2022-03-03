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

def transpose_matrix(matrix: np.ndarray) -> np.ndarray:
    """[summary]\n
    Transpose a matrix

    Arguments:
        matrix {np.ndarray} -- Matrix to be transposed

    Returns:
        np.ndarray -- Transposed matrix
    """
    return matrix.T

if __name__ == "__main__":
    # ?#### Creates a Matrix to be used in the next snippet
    the_matrix = CreateMatrixArray(BASIC_ARRAY_1, BASIC_ARRAY_2)

    # ?#### Prints the matrix
    print(f'Matrix: \n{the_matrix}')

    # ?#### Raises each element of the matrix to a power
    transposed_matrix = transpose_matrix(the_matrix)

    # ?#### Prints the matrix transposed
    print(f'Transposed Matrix: \n{transposed_matrix}')
