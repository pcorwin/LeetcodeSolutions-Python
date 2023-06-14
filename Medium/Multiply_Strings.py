#Multiply Strings

#Given two non-negative integers num1 and num2 represented as strings,
#   return the product of num1 and num2, also represented as a string.
#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly

#Constraints:
#   1 <= num1.length, num2.length <= 200
#   num1 and num2 consist of digits only.
#   Both num1 and num2 do not contain any leading zero, except the number 0 itself

def multiply(num1: str, num2: str):
    if len(num1) >= 1 and len(num2) <= 200:
        return str(int(num1) * int(num2))

def main():
    testcases = [
        ["2","3"],
        ["123","456"]
    ]
    for i in testcases:
        print(f'num1 = "{i[0]}", nums2 = "{i[1]}"\noutput = {multiply(i[0],i[1])}\n')


main()