class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        
        for path in paths:
            root, *docs = path.split()
            for doc in docs:
                key = re.search(r'\((\w+)\)', doc).group()
                files[key].append(f"{root}/{doc.replace(key, '')}")

            
        return (res for res in files.values() if len(res) > 1)
            
        
        