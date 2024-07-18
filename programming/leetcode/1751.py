class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        return keysPressed[max(range(len(releaseTimes)), key=lambda i : ((releaseTimes[i] - (releaseTimes[i - 1] if i else 0), ord(keysPressed[i]))))]
        