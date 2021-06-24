keyMap = [['.', ';'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], [
    'm', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u'], ['v', 'w', 'x'], ['y', 'z']]


def kpc(s):
    if len(s) == 1:
        return keyMap[int(s[0])]
    outList = []
    for word in kpc(s[1:]):
        for ch in keyMap[int(s[0])]:
            outList.append(ch+word)
    return outList


def main():
    s = input()
    out = kpc(s)
    print(out)


main()
