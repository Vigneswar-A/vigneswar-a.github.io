morse = str.maketrans(dict(zip((chr(i) for i in range(97 , 123)) ,[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])))
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(word.translate(morse) for word in words))
        