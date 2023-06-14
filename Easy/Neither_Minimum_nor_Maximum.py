#Neither Minimum nor Maximum

#Given an integer array nums containing distinct positive integers,
#   find and return any number from the array that is neither the minimum nor the maximum value in the array,
#   or -1 if there is no such number.
#Return the selected integer

#Constraints:
#   1 <= nums.length <= 100
#   1 <= nums[i] <= 100
#   All values in nums are distinct

def findNonMinOrMax(nums):
    if len(nums) > 2:
        nums.remove(max(nums))
        nums.remove(min(nums))
        if nums is not None:
            return nums[0]
    return -1

def main():
    testcases = [
        [3,2,1,4],
        [1,2],
        [2,1,3]
    ]
    for i in testcases:
        print(f'nums = {i}\noutput = {findNonMinOrMax(i)}\n')


main()