#Regular Expression Matching

#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#   '.' Matches any single character.
#   '*' Matches zero or more of the preceding element.
#   The matching should cover the entire input string (not partial).

#Constraints
#   1 <= s.length <= 20
#   1 <= p.length <= 20
#   s contains only lowercase English letters.
#   p contains only lowercase English letters, '.', and '*'.
#   It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

def isMatch(s, p):
    r = len(s)
    c = len(p)
    if (r == 0 and c == 0):
        return True
    if c == 0:
        return False

    d = [[False for a in range(c + 1)] for b in range(r + 1)]
    d[0][0] = True

    for i in range(2, c + 1):
        if p[i - 1] == '*':
            d[0][i] = d[0][i - 2]

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                d[i][j] = d[i - 1][j - 1]
            elif j > 1 and p[j - 1] == '*':
                d[i][j] = d[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    d[i][j] = d[i][j] or d[i - 1][j]
    return d[r][c]

def main():
    testcases = [
        ["aa", "a*"],
        ["ab", ".*"]
    ]
    for i in testcases:
        print(f's = {i[0]}\np = {i[1]}\noutput = {isMatch(i[0], i[1])}\n')


main()
