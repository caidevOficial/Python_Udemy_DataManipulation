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

BASIC_ARRAY_1 = [1, 2, 3, 4, 5]
BASIC_ARRAY_2 = [6, 7, 8, 9, 10]

def SetTypeOfArray(array: np.ndarray, type: str) -> np.ndarray:
    """[summary]
    Sets the type of an array
    Args:
        array (np.ndarray): [Array to be changed]
        type (str): [Type of the array]
    Returns:
        [np.ndarray]: [Array with the new type]
    """
    return array.astype(type)

def CreateMatrixArray(*args: np.ndarray) -> np.ndarray:
    """[summary]
    Creates a matrix array from a list of arrays
    Args:
        *args (np.ndarray): [The arrays to be added to the matrix]
    Returns:
        np.ndarray: [The matrix array]
    """
    return np.array(args)

