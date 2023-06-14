#Fizz Buzz

#Given an integer n, return a string array answer (1-indexed) where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

#Constraints:
#   1 <= n <= 10


def fizzBuzz(n):
    l = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        else:
            l.append(str(i))
    return l

def main():
    testcases = [
        3,
        5,
        15
    ]
    for i in testcases:
        print(f'n = {i}\noutput = {fizzBuzz(i)}\n')


main()