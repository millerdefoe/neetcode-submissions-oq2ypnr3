class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asStack = []
        for a in asteroids:
            while len(asStack) > 0 and a < 0 and asStack[-1] > 0: #collision event
                if abs(a) > asStack[-1]:
                    asStack.pop()
                elif abs(a) == asStack[-1]:
                    asStack.pop()
                    a = 0
                else:
                    a = 0
                    continue
                    
            if a:
                asStack.append(a)

        return asStack
                    

