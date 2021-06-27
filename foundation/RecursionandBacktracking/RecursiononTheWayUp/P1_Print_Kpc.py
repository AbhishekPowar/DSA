# 1. You are given a string str. The string str will contains numbers only,
# where each number stands for a key pressed on a mobile phone.
# 2. The following list is the key to characters map
# 0 -> .;
# 1 -> abc
# 2 -> def
# 3 -> ghi
# 4 -> jkl
# 5 -> mno
# 6 -> pqrs
# 7 -> tu
# 8 -> vwx
# 9 -> yz
# Use sample input and output to take idea about output.

# Sample Input
# 78
# Sample Output
# tv tw tx uv uw ux
# Same but just print

keyMap = [['.', ';'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u'], ['v', 'w', 'x'], ['y', 'z']]


def keyPadCartesian(s, temp):
    if len(s) == 0:
        print(temp)
    else:
        for ch in keyMap[int(s[0])]:
            keyPadCartesian(s[1:], temp+ch)


def main():
    s = input()
    keyPadCartesian(s, '')


main()
