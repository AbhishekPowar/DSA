# 1. You are given a number n and a number m representing number of rows and columns in a maze.
# 2. You are standing in the top-left corner and have to reach the bottom-right corner. Only two moves are allowed 'h' (1-step horizontal) and 'v' (1-step vertical).
# 3. Complete the body of getMazePath function - without changing signature - to get the list of all paths that can be used to move from top-left to bottom-right.
# Use sample input and output to take idea about output.

# Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.
# Input Format
# A number n
# A number m
# Output Format
# Contents of the arraylist containing paths as shown in sample output

# Sample Input
# 3
# 3
# Sample Output
# [hhvv, hvhv, hvvh, vhhv, vhvh, vvhh]


# def solve(sr,sc,dr,dc):
    # pathList=[]
    # def findAllPaths(sr,sc,dr,dc,path=''):
        # if sr==dr and sc==dc:
            # pathList.append(path)
        # elif sr>dr or sc>dc:
            # pass
        # else:
            # findAllPaths(sr+1,sc,dr,dc,path+'v')
            # findAllPaths(sr,sc+1,dr,dc,path+'h')
    # findAllPaths(sr,sc,dr,dc)
    # return pathList
def mazePath(sr,sc,dr,dc):
    if sr==dr and sc==dc:
        return [''] 
    elif sr>dr or sc>dc:
        return []
    allPath=[]
    for path in mazePath(sr,sc+1,dr,dc):
        allPath.append('h'+path)
    for path in mazePath(sr+1,sc,dr,dc):
        allPath.append('v'+path)
    return allPath    

def main():
    N=int(input())
    output=mazePath(0,0,N-1,N-1)
    print(output)

main()

