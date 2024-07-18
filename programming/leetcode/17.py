phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return map(''.join , product(*(phone[i] for i in map(int , digits))))
        