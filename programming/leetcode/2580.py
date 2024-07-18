class Solution:
    def isCircularSentence(self, sentence: str) -> bool:   
        return len(re.findall(r"(?<=(.)) (?=\1)", sentence)) == sentence.count(" ") and sentence[-1] == sentence[0]
        