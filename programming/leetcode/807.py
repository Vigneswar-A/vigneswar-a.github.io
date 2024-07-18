class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap=dict((order[i],i+1) for i in range(len(order)))
        return ''.join(sorted(s,key=lambda n:hashmap.get(n) or float('inf')))
        