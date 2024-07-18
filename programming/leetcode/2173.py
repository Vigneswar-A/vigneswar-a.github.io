class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        pattern = re.compile("[aA-zZ]+(-)?(?(1)[aA-zZ]+|[aA-zZ]*)[,.!]?|[,.!]{1}")
        return sum(1 for word in sentence.split() if pattern.fullmatch(word))
        
        