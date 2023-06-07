#Permutations

#Given an array nums of distinct integers, return all the possible permutations.
#You can return the answer in any order.



#Constraints:
#   1 <= nums.length <= 6
#   -10 <= nums[i] <= 10
#   All the integers of nums are unique.

def permute(nums):
    if len(nums) < 1:
        return [nums]
    l1 = []
    h(nums, l1, [])
    return l1

def h(n, l, p):
    for i in range(len(n)):
        h(n[:i] + n[i + 1:], l, p + [n[i]])
    if len(n) == 0:
        l.append(p)

def main():
    testcases = [
        [1, 2, 3],
        [0, 1],
        [1]
    ]
    for i in testcases:
        print(f'nums = {i}\noutput = {permute(i)}\n')


main()