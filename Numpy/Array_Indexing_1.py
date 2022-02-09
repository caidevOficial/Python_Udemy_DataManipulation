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

from Array_Example_2 import ARRAY1 as A1
from Array_Example_2 import ARRAY2 as A2
from Array_Example_2 import AddArrays


def PrintSingleArrayByIndex(array: np.ndarray, index: int) -> None:
    """[summary]
    Prints an array by index
    Args:
        array (np.ndarray): [The array to be printed]
        index (int): [Index of the array to be printed]
    """
    print(f'Index: {index}')
    print(f'Value: {array[index]}')

def PrintSingleElementByIndex(array: np.ndarray, index: int, elementIndex: int) -> None:
    """[summary]
    Prints the info of the array at the selected index and the info of the element at the selected elementIndex
    Args:
        array (np.ndarray): [2D Array to be printed]
        index (int): [Index of the array selected inside of the 2D array]
        elementIndex (int): [Index of the element selected inside of the array selected]
    """
    PrintSingleArrayByIndex(array, index)
    print(f'Element Selected: {array[index][elementIndex]}')
    

if __name__ == '__main__':
    PrintSingleElementByIndex(AddArrays(A1, A2), 0, 4)
