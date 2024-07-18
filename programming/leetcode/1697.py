class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict[0])):
            if len(set([w[:i]+w[i+1:] for w in dict])) < len(dict):
                return True
        return False
        