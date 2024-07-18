import re
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        return re.findall(r"(?<=\b"+f"{first} {second} )"+"(\w+)",text)
        