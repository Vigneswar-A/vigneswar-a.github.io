class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        counts = [Counter(word) for word in words]

        res = []
        i = j = 0
        while i < len(counts):
            j = i
            while j+1 < len(counts) and counts[j] == counts[j+1]:
                j += 1
            res.append(words[i])
            i = j+1

        return res
