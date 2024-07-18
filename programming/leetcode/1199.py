class Solution:
    def toHexspeak(self, num: str) -> str:

        res = hex(int(num))[2:].upper().replace("1", "I").replace("0", "O")
        return res if set(res) < {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'} else "ERROR"