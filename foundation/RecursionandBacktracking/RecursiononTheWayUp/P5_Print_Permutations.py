def printPermutation(s, temp):
    if len(s) == 0:
        print(temp)
    else:
        for i in range(0, len(s)):
            ch = s[i]
            rest = s[:i]+s[i+1:]
            printPermutation(rest, temp+ch)


def perm(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        return [s, s[::-1]]
    else:
        temp = []
        for i in range(0, len(s)):
            ch = s[i]
            rest = s[:i]+s[i+1:]
            for word in perm(rest):
                temp.append(ch+word)
        return temp


if __name__ == "__main__":
    s = 'dbc'
    printPermutation(s, '')
    # print(perm(s))
