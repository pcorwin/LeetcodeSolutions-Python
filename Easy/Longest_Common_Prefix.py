#Longest Common Prefix

#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

#Constraints:
#   1 <= strs.length <= 200
#   0 <= strs[i].length <= 200
#   strs[i] consists of only lowercase English letters.

def longestCommonPrefix(strs):
    r = ""
    i = 0
    size = len(strs)
    if size == i:
        return r
    elif size == 1:
        return strs[i]
    strs.sort()
    end = min(len(strs[i]), len(strs[size - 1]))
    while (i < end and strs[0][i] == strs[size - 1][i]):
        i += 1
    r = strs[0][0:i]
    return r

def main():
    testcases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"]
    ]
    for i in testcases:
        print(f'strs = {i}\n\noutput = {longestCommonPrefix(i)}\n')


main()