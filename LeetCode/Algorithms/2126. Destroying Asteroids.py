class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids = sorted(asteroids)
        newMass = mass
        for i in asteroids:
            if newMass >= i:
                newMass += i
            else:
                return False
        return True
