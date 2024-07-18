class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(map(lambda s : str.capitalize(s) if len(s) > 2 else s.lower() , title.split()))
        