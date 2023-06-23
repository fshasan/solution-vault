class Solution(object):
    def fizzBuzz(self, n):
        lst = []
        for i in range(1, n+1):
            if (i % 3 == 0) and (i % 5) == 0:
                string = "FizzBuzz"
                lst.append(string)
            elif i % 3 == 0:
                string = "Fizz"
                lst.append(string)    
            elif i % 5 == 0:
                string = "Buzz"
                lst.append(string)
            else:
                string = str(i)
                lst.append(string)
        return lst