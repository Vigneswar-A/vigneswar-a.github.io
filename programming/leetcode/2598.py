class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        back = front = startIndex
        dist = 0
        end = len(words) - startIndex
        size = len(words)

        while dist < size:
            if words[back] == target or words[front] == target:
                return dist
            dist += 1
            front = (front+1)%size
            back -= 1
            
        return -1
            
