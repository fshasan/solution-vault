class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = sorted(candies)[-1]
        ans_lst = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                ans_lst.append(True)
            else:
                ans_lst.append(False)

        return ans_lst