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
from Array_Example_1 import PrintArrayInfo as EA1
from Common_Variables import ARRAY1, ARRAY2
from Common_Variables import AddArrays

def MultiplyArrayValues(array: list, multiplier: int) -> list:
    """[summary]
    Multiplies all the values of the array by the multiplier
    Args:
        array (list): [The array to be multiplied]
        multiplier (int): [The multiplier]
    """
    return np.array(array) * multiplier

def ThreeDimentionsArray(*args: list) -> None:
    """[summary]
    Prints the array and its description
    Args:
        array (list): [The array to be printed and described]
    """
    array3d = np.array(args)
    EA1(array3d)


if __name__ == '__main__':
    
    twoDarrayA = AddArrays(
            MultiplyArrayValues(ARRAY1, 3),
            MultiplyArrayValues(ARRAY2, 2)
        )
    twoDarrayB = AddArrays(
            MultiplyArrayValues(ARRAY2, 2),
            MultiplyArrayValues(ARRAY1, 4)
        )

    ThreeDimentionsArray(twoDarrayA, twoDarrayB)
