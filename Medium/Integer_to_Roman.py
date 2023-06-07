#Integer to Roman

#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
#For example, 2 is written as II in Roman numeral, just two one's added together.
#12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
#Roman numerals are usually written largest to smallest from left to right.
#However, the numeral for four is not IIII. Instead, the number four is written as IV.
#Because the one is before the five we subtract it making four.
#The same principle applies to the number nine, which is written as IX.

#There are six instances where subtraction is used:
#   I can be placed before V (5) and X (10) to make 4 and 9.
#   X can be placed before L (50) and C (100) to make 40 and 90.
#   C can be placed before D (500) and M (1000) to make 400 and 900.

#Given an integer, convert it to a roman numeral.

#Constraints:
#   1 <= num <= 3999

import math

def intToRoman(num):
    romans = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    d = 1
    while num >= d:
        d *= 10
    d /= 10
    r = ""
    while num:
        lNum = int(num / d)

        if lNum <= 3:
            r += (romans[d] * lNum)
        elif lNum == 4:
            r += (romans[d] + romans[d * 5])
        elif 5 <= lNum <= 8:
            r += (romans[d * 5] + (romans[d] * (lNum - 5)))
        elif lNum == 9:
            r += (romans[d] + romans[d * 10])

        num = math.floor(num % d)
        d /= 10

    return r

def main():
    testcases = [
        3,
        58,
        1994
    ]
    for i in testcases:
        print(f'nums = {i}\noutput = {intToRoman(i)}\n')


main()