def cartesianProduct(a, b):
    c = []
    for i in a:
        for j in b:
            c.append(i+j)
    return c


def KeyMapCartesianHandler(dyn, alist):
    out = cartesianProduct(dyn, alist[0])
    if len(alist) > 1:
        return KeyMapCartesianHandler(out, alist[1:])
    return out


def main():
    keyMap = [['.', ';'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], [
        'm', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u'], ['v', 'w', 'x'], ['y', 'z']]
    s = '789'
    args = []
    for i in s:
        args.append(keyMap[int(i)])
    out = KeyMapCartesianHandler(args[0], args[1:])
    print(out)

main()
