class Solution:
    def longestWord(self, words: List[str]) -> str:
        set_of_words = set(words)
        max_word = ''
        maxlen = 0
        for word in words:
            flag = True
            for i in range(1 , len(word)):
                if word[:i] not in set_of_words:
                    flag = False
                    break
            if flag:
                if (l := len(word)) > maxlen:
                    max_word = word
                    maxlen = l
                elif l == maxlen:
                    max_word = min(max_word , word)

        return max_word
        