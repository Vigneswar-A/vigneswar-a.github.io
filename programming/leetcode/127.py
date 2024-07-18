class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dist = 0
        queue = deque([beginWord])
        visited = set()
        wordList = set(wordList)
        while queue:
            dist += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == endWord:
                    return dist
                for i in range(len(node)):
                    for c in string.ascii_lowercase:
                        diffword = node[:i] + c + node[i+1:]
                        if diffword in wordList:
                            queue.append(diffword)

        return 0
                
        