#Valid Parentheses

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#   determine if the input string is valid.
#An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
#   Every close bracket has a corresponding open bracket of the same type

#Constraints:
#   1 <= s.length <= 104
#   s consists of parentheses only '()[]{}'.


def isValid(s):
    open_list = ['(' ,'[' ,'{']
    close_list = [')' ,']' ,'}']
    l = []
    for i in s:
        if i in open_list:
            l.append(i)
        elif i in close_list:
            loc = close_list.index(i)
            if ((len(l) > 0) and (open_list[loc] == l[len(l ) -1])):
                l.pop()
            else:
                return False
    if len(l) == 0:
        return True
    return False

def main():
    testcases = [
        "()",
        "()[]{}",
        "(]"
    ]
    for i in testcases:
        print(f's = "{i}"\noutput = {isValid(i)}\n')


main()