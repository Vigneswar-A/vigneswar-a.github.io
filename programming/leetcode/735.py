class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                flag = True
                while stack and stack[-1] > 0 and -asteroid >= stack[-1] and flag:
                    if -asteroid == stack[-1]:
                        flag = False
                    stack.pop()
                if (not stack or stack[-1] < 0) and flag:
                    stack.append(asteroid)
        return stack