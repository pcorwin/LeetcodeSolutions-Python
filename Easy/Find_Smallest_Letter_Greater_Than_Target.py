#Find Smallest Letter Greater Than Target

#You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
#There are at least two different characters in letters.
#Return the smallest character in letters that is lexicographically greater than target.
#If such a character does not exist, return the first character in letters.

#Constraints:
#   2 <= letters.length <= 104
#   letters[i] is a lowercase English letter.
#   letters is sorted in non-decreasing order.
#   letters contains at least two different characters.
#   target is a lowercase English letter.

def nextGreatestLetter(letters, target):
    for i in letters:
        if target < i:
            return i
    return letters[0]

def main():
    testcases = [
        [["c","f","j"], "a"],
        [["c","f","j"], "c"],
        [["x","x","y","y"], "z"]
    ]
    for i in testcases:
        print(f'letters = {i[0]}, target = "{i[1]}"\noutput = {nextGreatestLetter(i[0],i[1])}\n')

main()