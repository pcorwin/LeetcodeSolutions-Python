#Search a 2D Matrix

#You are given an m x n integer matrix matrix with the following two properties:

#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.

#You must write a solution in O(log(m * n)) time complexity

#Constraints:
#   m == matrix.length
#   n == matrix[i].length
#   1 <= m, n <= 100
#   -104 <= matrix[i][j], target <= 104

def searchMatrix(matrix, target):
    for x in matrix:
        if target in x:
            return True
    return False

def main():
    testcases = [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13]
    ]
    for i in testcases:
        print(f'nums = {i}\noutput = {searchMatrix(i[0], i[1])}\n')

main()