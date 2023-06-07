#Reverse Integer

#Given a signed 32-bit integer x, return x with its digits reversed.
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#Constraints:
#   -231 <= x <= 231 - 1

def reverse(x):
    upper = ((2 ** 31) - 1)
    lower = -2 ** 31
    s = str(x)[::-1]
    if x < 0:
        s = "-" + s[:len(s) - 1]
    if lower < int(s) < upper:
        return int(s)
    else:
        return 0

def main():
    testcases = [
        123,
        -321,
        120
    ]
    for i in testcases:
        print(f'input = {i}\noutput = {reverse(i)}\n')


main()