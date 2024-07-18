class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        counts = Counter()
        for msg,sender in zip(messages, senders):
            counts[sender] += msg.count(' ')+1
            
        return max(counts, key=lambda i : (counts.get(i), i))
        