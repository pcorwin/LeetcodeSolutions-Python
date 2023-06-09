#Majority Element

#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times.
#You may assume that the majority element always exists in the array.

#Constraints:
#   n == nums.length
#   1 <= n <= 5 * 104
#   -109 <= nums[i] <= 10

def majorityElement(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    maj_el = max(d, key=d.get)
    return maj_el

def main():
    testcases = [
        [3,2,3],
        [2,2,1,1,1,2,2]
    ]
    for i in testcases:
        print(f'nums = {i}\noutput = {majorityElement(i)}\n')

main()