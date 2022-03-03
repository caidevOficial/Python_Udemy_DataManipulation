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

def min_value_of_matrix(matrix: np.ndarray) -> int:
    """[summary]
    Find the minimum value of a matrix

    Args:
        matrix (np.ndarray): [The matrix to be searched]

    Returns:
        int: [The minimum value]
    """
    return np.min(matrix)

def max_value_of_matrix(matrix: np.ndarray) -> int:
    """[summary]
    Find the maximum value of a matrix

    Args:
        matrix (np.ndarray): [The matrix to be searched]

    Returns:
        int: [The maximum value]
    """
    return np.max(matrix)

def sum_of_matrix_values(matrix: np.ndarray) -> int:
    """[summary]
    Find the sum of a matrix

    Args:
        matrix (np.ndarray): [The matrix to be searched]

    Returns:
        int: [The sum of the matrix]
    """
    return np.sum(matrix)

def mean_of_matrix_values(matrix: np.ndarray) -> float:
    """[summary]
    Find the mean of a matrix

    Args:
        matrix (np.ndarray): [The matrix to be searched]

    Returns:
        float: [The mean of the matrix]
    """
    return np.mean(matrix)

def median_of_matrix_values(matrix: np.ndarray) -> float:
    """[summary]
    Find the median of a matrix

    Args:
        matrix (np.ndarray): [The matrix to be searched]

    Returns:
        float: [The median of the matrix]
    """
    return np.median(matrix)

def variance_of_matrix_values(matrix: np.ndarray) -> float:
    """[summary]
    Find the variance of a matrix

    Args:
        matrix (np.ndarray): [The matrix to be searched]

    Returns:
        float: [The variance of the matrix]
    """
    return np.var(matrix)

def standard_deviation_of_matrix_values(matrix: np.ndarray) -> float:
    """[summary]
    Find the standard deviation of a matrix

    Args:
        matrix (np.ndarray): [The matrix to be searched]

    Returns:
        float: [The standard deviation of the matrix]
    """
    return np.std(matrix)

if __name__ == "__main__":

    # ?#### Creates the matrix
    the_matrix = CreateMatrixArray(BASIC_ARRAY_1, BASIC_ARRAY_2)
    # ?### Test min_value_of_matrix
    print("Min value of matrix: \n", min_value_of_matrix(the_matrix))
    print("Max value of matrix: \n", max_value_of_matrix(the_matrix))
    print("Sum of matrix values: \n", sum_of_matrix_values(the_matrix))
    print("Mean of matrix values: \n", mean_of_matrix_values(the_matrix))
    print("Median of matrix values: \n", median_of_matrix_values(the_matrix))
    print("Variance of matrix values: \n", variance_of_matrix_values(the_matrix))
    print("Standard deviation of matrix values: \n", standard_deviation_of_matrix_values(the_matrix))