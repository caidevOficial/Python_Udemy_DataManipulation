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

def CreateZeroArray(size: int) -> np.ndarray:
    """[summary]
    Creates an array of zeros
    Args:
        size (int): [Size of the array]
    Returns:
        [np.ndarray]: [Array of zeros]
    """
    return np.zeros(size)


if __name__ == "__main__":
    print(CreateZeroArray(5))
    print(f'Int Type: {SetTypeOfArray(CreateZeroArray(5), "int")}')
    print(f'Float Type: {SetTypeOfArray(CreateZeroArray(5), "float")}')
    print(f'String Type: {SetTypeOfArray(CreateZeroArray(5), "str")}')
    print(f'Bool Type: {SetTypeOfArray(CreateZeroArray(5), "bool")}')
    print(f'Complex Type: {SetTypeOfArray(CreateZeroArray(5), "complex")}')
    print(f'Object Type: {SetTypeOfArray(CreateZeroArray(5), "object")}')
    print(f'Unicode Type: {SetTypeOfArray(CreateZeroArray(5), "unicode")}')
    print(f'Byte Type: {SetTypeOfArray(CreateZeroArray(5), "byte")}')
    print(f'Unsigned Int Type: {SetTypeOfArray(CreateZeroArray(5), "uint")}')
    