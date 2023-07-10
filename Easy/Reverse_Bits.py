#Reverse Bits

#Reverse bits of a given 32 bits unsigned integer.

#Note:

#Note that in some languages, such as Java, there is no unsigned integer type.
#In this case, both input and output will be given as a signed integer type.
#They should not affect your implementation, as the integer's internal binary representation
#   is the same, whether it is signed or unsigned.
#In Java, the compiler represents the signed integers using 2's complement notation.
#Therefore, in Example 2 above, the input represents the signed integer -3 and
#   the output represents the signed integer -1073741825.

import time

class Solution:
    def __init__(self):
        self.testcases = [0b00000010100101000001111010011100,
                          0b11111111111111111111111111111101]
        self.solutions = []
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            if n >> i & 1:
                result |= 1 << 31 - i
        return result
    def solve(self):
        for i in self.testcases:
            self.solutions.append(self.reverseBits(i))
    def print(self, t):
        print("Reverse Bits")
        for i in range(len(self.testcases)):
            print(f"\tinput: {self.testcases[i]}\n\toutput: {self.solutions[i]}\n")
        print(f"\ttime: {t}\n")

def run():
    s = Solution()
    t0 = time.time()
    s.solve()
    t1 = time.time()
    t = (t1 - t0)
    s.print(t)