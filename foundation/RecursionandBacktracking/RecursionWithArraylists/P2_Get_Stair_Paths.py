# def findAllPaths(N):
    # allPathList=[]
    # def allPaths(path, target):
        # if target > 0:
            # for i in range(1, 4):
                # allPaths(path+f'{i}', target-i)
        # elif target == 0:
            # allPathList.append(path)
    # allPaths('', N)
    # return [int(path) for path in allPathList]

# def findAllPathsInt(N):
    # allPathList=[]
    # def allPaths(path, target):
        # if target > 0:
            # for i in range(1, 4):
                # allPaths(path*10+i, target-i)
        # elif target == 0:
            # allPathList.append(path)
    # allPaths(0, N)
    # return allPathList
def findAllPaths(N):
    if N==1:
        return {1}
    allPathList={N}
    for ways in findAllPaths(N-1):
        allPathList.add(ways*10+1)
        allPathList.add(int(f"1{ways}"))
    return allPathList 


def main():
    N=int(input())
    allPathList=findAllPaths(N)
    print(allPathList)


main()
