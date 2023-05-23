class Solution(object):
    def average(self, salary):
        sum = 0
        for i in range(len(salary)):
            sum += salary[i]
        salary = sorted(salary)
        sum = sum - salary[0] - salary[-1]
        div = len(salary) - 2

        return float(sum) / div