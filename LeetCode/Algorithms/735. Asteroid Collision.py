class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        i = 0

        while i < len(asteroids):
            if len(stack) > 0 and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] > abs(asteroids[i]):
                    i += 1
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop(-1)
                    i += 1
                elif stack[-1] < abs(asteroids[i]):
                    stack.pop(-1)
            else:
                stack.append(asteroids[i])
                i += 1
        return stack
