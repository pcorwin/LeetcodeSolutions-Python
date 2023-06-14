#Reverse Vowels of a String

#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#Constraints:
#   1 <= s.length <= 3 * 105
#   s consist of printable ASCII characters.

def reverseVowels(s):
    vowels = ['A' ,'E' ,'I' ,'O' ,'U' ,'a' ,'e' ,'i' ,'o' ,'u']
    l = []
    s.split()
    outs = ''
    for i in s[::-1]:
        if i in vowels:
            l.append(i)
    x = 0
    for i in s:
        if i in vowels:
            outs += l[x]
            x+=1
        else:
            outs += i
    return outs

def main():
    testcases = [
        "hello",
        "leetcode"
    ]
    for i in testcases:
        print(f's = {i}\noutput = {reverseVowels(i)}\n')


main()