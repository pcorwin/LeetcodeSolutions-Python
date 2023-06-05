def findMedianSortedArrays(nums1, nums2):
    l = (nums1 + nums2)
    l.sort()
    x = len(l) / 2
    if len(l) % 2 != 0:
        return l[int(x)]
    else:
        return (l[int(x)] + l[int(x) - 1]) / 2


def main():
    testcases = [
        [[1, 3], [2]],
        [[1, 2], [3, 4]]
    ]
    for i in testcases:
        print(f'nums1 = {i[0]}\nnums2 = {i[1]}\noutput = {findMedianSortedArrays(i[0], i[1])}\n')


main()
