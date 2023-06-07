#Merge Sorted Array

def merge(nums1, m: int, nums2, n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for x in range(n):
        nums1.pop()
    if nums2 is not None:
        nums1.extend(nums2)
    nums1.sort()


def main():
    testcases = [
        [[1], 1, [], 0],
        [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
        [[0], 0, [1], 1]
    ]
    for i in testcases:
        print(f'nums1 = {i[0]}\nm = {i[1]}\nnums2 = {i[2]}\nn = {i[3]}\noutput = {merge(i[0], i[1], i[2], i[3])}\n')


main()
