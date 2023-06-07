#Maximum Gap

#Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
#If the array contains less than two elements, return 0.
#You must write an algorithm that runs in linear time and uses linear extra space.

#Constraints
#   1 <= nums.length <= 105
#   0 <= nums[i] <= 109

def maximumGap(nums):
    if len(nums) < 2:
        return 0
    else:
        nums.sort()
        if len(nums) == 2:
            return nums[1] - nums[0]
        else:
            c = 0
            for x in range(len(nums)):
                if (nums[x] - nums[x - 1]) > c:
                    c = nums[x] - nums[x - 1]
            return c

def main():
    testcases = [
        [3, 6, 9, 1],
        [10]
    ]
    for i in testcases:
        print(f'nums = {i}\noutput = {maximumGap(i)}\n')


main()