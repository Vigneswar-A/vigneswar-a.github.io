class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)
            
        for string in strings:
            x = ord(string[0])
            res[tuple(map(lambda c:(ord(c) - x)%26, string))].append(string)

        return res.values()
        