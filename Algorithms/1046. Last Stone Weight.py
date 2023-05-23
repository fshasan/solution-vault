class Solution(object):
    def lastStoneWeight(self, stones):
        while(True):
            stones = sorted(stones)
            if len(stones) == 1:
                ans = stones[-1]
                break
            elif len(stones) == 0:
                return 0
            else:
                if stones[-2] != stones[-1]:
                    stones[-1] = stones[-1] - stones[-2]
                    stones.pop(-2)
                elif stones[-1] == stones[-2]:
                    stones.pop(-1)
                    stones.pop(-1)
        return ans