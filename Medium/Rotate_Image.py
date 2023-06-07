#Rotate Image

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#DO NOT allocate another 2D matrix and do the rotation.

#Constraints:
#   n == matrix.length == matrix[i].length
#   1 <= n <= 20
#   -1000 <= matrix[i][j] <= 1000

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
def main():
    testcases = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    ]
    for i in testcases:
        print(f'matrix = {i}')
        rotate(i)
        print(f'output = {i}\n')

main()