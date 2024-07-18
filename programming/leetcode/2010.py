t=str().maketrans({'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9'})
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return int(firstWord.translate(t))+int(secondWord.translate(t))==int(targetWord.translate(t))
        