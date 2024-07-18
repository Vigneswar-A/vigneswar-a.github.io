class Solution:
	def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
		a,b=sorted([start,destination])
		return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))