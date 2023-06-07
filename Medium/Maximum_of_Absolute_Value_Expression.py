#Maximum of Absolute Value Expression

#Given two arrays of integers with equal lengths, return the maximum value of:
#   |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
#   where the maximum is taken over all 0 <= i, j < arr1.length

#Constraints:
#   2 <= arr1.length == arr2.length <= 40000
#   -10^6 <= arr1[i], arr2[i] <= 10^6

def maxAbsValExpr(arr1, arr2):
    n = len(arr1)
    a = [arr1[i] + arr2[i] + i for i in range(n)]
    b = [arr1[i] + arr2[i] - i for i in range(n)]
    c = [arr1[i] - arr2[i] + i for i in range(n)]
    d = [arr1[i] - arr2[i] - i for i in range(n)]
    return max(map(lambda x: max(x) - min(x), (a, b, c, d)))

def main():
    testcases = [
        [[1,2,3,4],[-1,4,5,6]],
        [[1,-2,-5,0,10],[0,-2,-1,-7,-4]]
    ]
    for i in testcases:
        print(f'arr1 = {i[0]}, arr2 = {i[1]}\noutput = {maxAbsValExpr(i[0],i[1])}\n')

main()