class Solution:

    # not needed
    def orderlyQueueExtraLogic(self, s: str, k: int) -> str:
        '''
        Logic:
            Solution optimized there are no cycles abcabc

            s = c a b a b a x
            calculate least of currentArray and save it in left
            in right save letter next ot minimun char

            least char | currentArray 
            -----------+--------------
            None       | ['c', 'a', 'b', 'a', 'b', 'a', 'x']
            a          | ['b', 'b', 'x']
            b          | ['a', 'a']
            a          | ['b', 'x']
            b          | ['a']

        '''
        N = len(s)
        if k == 1:
            idxs = [i for i in range(N)]
            count = 0
            while len(idxs) > 1:
                count += 1
                mini = min(idxs, key=lambda x: s[x])
                idxs = [(i+1) % N for i in idxs if s[mini] == s[i]]
                if count*2 == N:
                    break
            start = idxs[0]-count
            return s[start:]+s[:start]

        if k >= 2:
            return ''.join(sorted(s))

    def orderlyQueue(self, s: str, k: int) -> str:
        N = len(s)
        if k == 1:
            mini = s
            for _ in range(N):
                s = s[1:]+s[0]
                mini = min(mini, s)
            return mini
        if k >= 2:
            return ''.join(sorted(s))

    def orderlyQueueOptimized(self, s: str, k: int) -> str:
        N = len(s)
        if k == 1:
            return min([s[i:]+s[:i] for i in range(N)])
        return ''.join(sorted(s))


if __name__ == "__main__":
    s = 'cababax'
    k = 1
    output = Solution().orderlyQueueExtraLogic(s, 1)
    print(output)
