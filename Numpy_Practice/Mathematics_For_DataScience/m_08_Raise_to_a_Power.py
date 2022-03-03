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

def raise_to_a_power(array: np.ndarray, power: int) -> np.ndarray:
    """[summary]\n
    Raises each element of an array to a power
    
    Args:
        array (np.ndarray): [The array to be modified]
        power (int): [The power to be applied]
    Returns:
        np.ndarray: [The modified array]
    """
    return array ** power

if __name__ == '__main__':
    # ?#### Creates a Matrix to be used in the next snippet
    matrix = CreateMatrixArray(BASIC_ARRAY_1, BASIC_ARRAY_2)
    
    # ?#### Prints the matrix
    print(f'Matrix: \n{matrix}')
    
    # ?#### Raises each element of the matrix to a power
    matrix_powered = raise_to_a_power(matrix, 2)

    # ?#### Prints the matrix powered
    print(f'Raise to power: \n{matrix_powered}')