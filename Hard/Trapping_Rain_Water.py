#Trapping Rain Water

#Given n non-negative integers representing an elevation map where the width of each bar is 1,
#   compute how much water it can trap after raining.

#Constraints:
#   n == height.length
#   1 <= n <= 2 * 104
#   0 <= height[i] <= 105

def trap(height):
    l = 0
    r = len(height) - 1
    lmax = height[l]
    rmax = height[r]
    water = 0

    while l < r:
        if lmax < rmax:
            l += 1
            lmax = max(lmax, height[l])
            water += lmax - height[l]
        else:
            r -= 1
            rmax = max(rmax, height[r])
            water += rmax - height[r]

    return water

def main():
    testcases = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5]
    ]
    for i in testcases:
        print(f'height = {i}\noutput = {trap(i)}\n')

main()