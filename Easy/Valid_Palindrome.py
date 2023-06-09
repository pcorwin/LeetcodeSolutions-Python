#Valid Palindrome

#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
#   non-alphanumeric characters, it reads the same forward and backward.
#Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

#Constraints:

#1 <= s.length <= 2 * 105
#s consists only of printable ASCII characters.

def isPalindrome(s):
    a = s.lower()
    a = ''.join(c for c in a if c.isalnum())
    b = a[::-1]
    if a == b:
        return True
    return False

def main():
    testcases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " "
    ]
    for i in testcases:
        print(f's = "{i}"\noutput = {isPalindrome(i)}\n')


main()