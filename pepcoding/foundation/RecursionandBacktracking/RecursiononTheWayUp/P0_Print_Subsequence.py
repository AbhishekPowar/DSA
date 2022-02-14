# 1. You are given a string str.  2. Complete the body of getSS function -
# without changing signature - to calculate all subsequences of str.  Use
# sample input and output to take idea about subsequences.

# Note -> The online judge can't force you to write the function recursively
# but that is what the spirit of question is.  Write recursive and not
# iterative logic. The purpose of the question is to aid learning recursion and
# not test you.  Input Format A string str Output Format Contents of the
# arraylist containing subsequences as shown in sample output

# Sample Input abc Sample Output [, c, b, bc, a, ac, ab, abc]
# Same as getSubSequence but just print no need to put it in a list


def printGetSubSequence(s, temp):
    if not s:
        print(temp)
    else:
        printGetSubSequence(s[1:], temp)
        printGetSubSequence(s[1:], temp+s[0])


def main():
    s = 'abc'
    printGetSubSequence(s, '')


main()
