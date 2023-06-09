#Rotate Array

#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#Constraints:
#   1 <= nums.length <= 105
#   -231 <= nums[i] <= 231 - 1
#   0 <= k <= 105

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)-1
    for i in range(k):
        nums.insert(0, nums[l])
        nums.pop()

def main():
    testcases = [
        [[1,2,3,4,5,6,7],3],
        [[-1,-100,3,99],2]
    ]
    for i in testcases:
        print(f'nums = {i[0]}, k = {i[1]}')
        rotate(i[0], i[1])
        print(f'{i[0]}\n')
main()