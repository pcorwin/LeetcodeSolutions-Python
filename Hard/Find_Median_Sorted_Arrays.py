#Median of Two Sorted Arrays

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n))

#Constraints:
#   nums1.length == m
#   nums2.length == n
#   0 <= m <= 1000
#   0 <= n <= 1000
#   1 <= m + n <= 2000
#   -106 <= nums1[i], nums2[i] <= 106

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
