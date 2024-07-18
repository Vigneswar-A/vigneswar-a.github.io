# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        differences = defaultdict(lambda : defaultdict(set))
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                diff = 6-sum(words[i][k] == words[j][k] for k in range(6))
                differences[words[i]][diff].add(words[j])
                differences[words[j]][diff].add(words[i])
            
        
        valids = set(words)
        for _ in range(30):
            if not valids:
                break
            diff = 6-master.guess(guess := valids.pop())
            valids = {w for w in valids if w in differences[guess][diff]}
            