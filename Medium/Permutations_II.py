#Permutations II

#Given a collection of numbers, nums, that might contain duplicates, return all possible unique
#   permutations in any order.

#Constraints:
#   1 <= nums.length <= 8
#   -10 <= nums[i] <= 10
def permuteUnique(nums):
    def h(n, p, l):
        if len(n) == 0:
            l.append(p)
            return
        for a in range(len(n)):
            h(n[:a] + n[ a +1:] ,p + [n[a]], l)

    nums.sort()
    l1 = []
    h(nums, [], l1)
    l1 = set(tuple(r) for r in l1)
    return list(l1)

def main():
    testcases = [
        [1, 1, 2],
        [1, 2, 3]
    ]
    for i in testcases:
        print(f'nums = {i}\noutput = {permuteUnique(i)}\n')

main()