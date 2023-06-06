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