#Two Sum

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#
#Constraints:
#   2 <= nums.length <= 104
#   -109 <= nums[i] <= 109
#   -109 <= target <= 109
#   Only one valid answer exists.


def twoSum(nums, target):
    groups = {}
    for i, j in enumerate(nums):
        if j in groups:
            return [groups[j], i]
        groups[target - j] = i


def main():
    testcases = [
        [[3, 2, 3], 6],
        [[2, 7, 11, 15], 9],
        [[3, 2, 4], 6],
        [[3, 3], 6]
    ]
    for i in testcases:
        print(f'nums = {i[0]}\ntarget = {i[1]}\noutput = {twoSum(i[0], i[1])}\n')


main()
