class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
	    i = 0
	    while i <= len(arr)-1:
		    if arr[i:i+m] * k == arr[i:i+m*k]:
			    return True

		    i += 1

	    return False
        