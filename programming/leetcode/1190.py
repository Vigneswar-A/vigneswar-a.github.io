class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        for region in regions[::-1]:
            if region1 in region and region2 in region:return region[0]
            if region1 in region:region1=region[0];continue
            if region2 in region:region2=region[0]