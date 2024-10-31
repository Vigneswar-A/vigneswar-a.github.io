class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        
        words = [word[::-1] for word in words]
        result = result[::-1]
        
        mapping = {}
        digits = set(range(10))
        max_len = max(map(len, words))
        def backtrack(digit_num, word_num, total, carry):
            if digit_num == len(result) and word_num == len(words):
                return (total+carry) == 0 and (len(result) == 1 or mapping.get(result[-1]) != 0)
            elif max_len+1 == len(result) and digit_num == max_len and ((carry in digits and mapping.get(result[-1]) is None) or carry == mapping.get(result[-1])) :
                return total == 0 and (len(result) == 1 or mapping.get(result[-1]) != 0)
            
            if word_num == len(words):
                digit = (total+carry)%10
                if mapping.get(result[digit_num]) is None:
                    if digit not in digits:
                        return False
                    mapping[result[digit_num]] = digit
                    digits.remove(digit)
                    if backtrack(digit_num+1, 0, 0, (total+carry)//10):
                        return True
                    digits.add(digit)
                    del mapping[result[digit_num]]
                elif mapping[result[digit_num]] == digit:
                    return backtrack(digit_num+1, 0, 0, (total+carry)//10)
                return False
            
            if digit_num >= len(words[word_num]):
                return backtrack(digit_num, word_num+1, total, carry)
            
            if mapping.get(words[word_num][digit_num]) is not None:
                if len(words[word_num]) > 1 and digit_num == len(words[word_num])-1 and mapping.get(words[word_num][digit_num]) == 0:
                    return False
                return backtrack(digit_num, word_num+1, total+mapping[words[word_num][digit_num]], carry)
            
            for digit in digits.copy():
                if len(words[word_num]) > 1 and digit_num == len(words[word_num])-1 and digit == 0:
                    continue
                mapping[words[word_num][digit_num]] = digit
                digits.remove(digit)
                if backtrack(digit_num, word_num+1, total+digit, carry):
                    return True
                digits.add(digit)
                del mapping[words[word_num][digit_num]]

            return False
                    
        return backtrack(0, 0, 0, 0)
    