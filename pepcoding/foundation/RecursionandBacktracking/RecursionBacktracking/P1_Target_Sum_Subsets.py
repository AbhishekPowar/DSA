# Print all the subset whose sum is equal to give target
# Sample Input
# 5
# 10,20,30,40,50
# Target 60
# Sample Output
# 10, 20, 30
# 10, 50,
# 20, 40

def getSubset(ar, target, temp, outputSet):
    if target == 0:
        outputSet.add(tuple(temp))
    if len(ar) != 0:
        getSubset(ar[1:], target, temp, outputSet)
        getSubset(ar[1:], target-ar[0], temp+[ar[0]], outputSet)
    return outputSet


def readInput():
    ar = []
    N = int(input())
    for _ in range(N):
        ar.append(int(input()))
    target = int(input())
    return ar, target


if __name__ == "__main__":
    ar, target = [10, 20, 30, 40, 50], 60
    output = getSubset(ar, target, [], set())
    print(output)
