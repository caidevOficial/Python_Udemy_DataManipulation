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
from Common_Variables import *

def DivScalarToArray(array: np.ndarray, scalar: int) -> np.ndarray:
    """[summary]
    Divide a scalar to each element of an array
    Args:
        array (np.ndarray): [The array to be modified]
        scalar (int): [The scalar to be divided]

    Returns:
        np.ndarray: [The modified array]
    """
    return array / scalar

def DivScalarToArrayGetInt(array: np.ndarray, scalar: int) -> np.ndarray:
    """[summary]
    Divide a scalar to each element of an array and 
    get a new array with only the integer part of the division.
    Args:
        array (np.ndarray): [The array to be modified only with integers]
        scalar (int): [The scalar to be divided]

    Returns:
        np.ndarray: [The modified array]
    """
    return array // scalar

if __name__ == '__main__':
    print(f'Array 1: {np.array(BASIC_ARRAY_1)}')
    print(f'Array 2: {np.array(BASIC_ARRAY_2)}')
    print(f'#### Simply Division ####')
    print(f'Div scalar to array 1: {DivScalarToArray(np.array(BASIC_ARRAY_1), 4)}')
    print(f'Div scalar to array 2: {DivScalarToArray(np.array(BASIC_ARRAY_2), 2)}')
    print(f'#### Integer Division ####')
    print(f'Div scalar to array 1: {DivScalarToArrayGetInt(np.array(BASIC_ARRAY_1), 4)}')
    print(f'Div scalar to array 2: {DivScalarToArrayGetInt(np.array(BASIC_ARRAY_2), 2)}')
    print(f'Original arrays: {CreateMatrixArray(np.array(BASIC_ARRAY_1), np.array(BASIC_ARRAY_2))}')
