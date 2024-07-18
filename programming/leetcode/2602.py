class Solution:
    def captureForts(self, forts: List[int]) -> int:
        return max(map(len, re.findall(r"(?<=(?<!-)1)0+(?=-1)|(?<=-1)0+(?=1)", "".join(map(str, forts)))), default = 0)
        
        