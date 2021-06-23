def findAllPaths(N):
    allPathList=[]
    def allPaths(path, target):
        if target > 0:
            for i in range(1, 4):
                allPaths(path+f'{i}', target-i)
        elif target == 0:
            allPathList.append(path)
    allPaths('', N)
    return [int(path) for path in allPathList]

def findAllPathsInt(N):
    allPathList=[]
    def allPaths(path, target):
        if target > 0:
            for i in range(1, 4):
                allPaths(path*10+i, target-i)
        elif target == 0:
            allPathList.append(path)
    allPaths(0, N)
    return allPathList

def main():
    N=int(input())
    allPathList=findAllPathsInt(N)
    print(allPathList)


main()
