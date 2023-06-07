#Longest SUbstring Without Repeating Characters

#Given a string s, find the length of the longest substring without repeating characters

#Constraints:
#   0 <= s.length <= 5 * 104
#   s consists of English letters, digits, symbols and spaces.


def lengthOfLongestSubstring(s):
    x = ""
    l = -1
    if len(s) < 2:
        return len(s)
    for a in list(s):
        sub = "".join(a)
        if sub in x:
            x = x[x.index(sub) + 1:]
        x = x + "".join(a)
        l = max(len(x), l)
    return l


def main():
    testcases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
    ]
    for i in testcases:
        print(f'substring = {i}\noutput = {lengthOfLongestSubstring(i)}\n')


main()
