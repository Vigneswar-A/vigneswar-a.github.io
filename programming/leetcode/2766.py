class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        C = []
        a_counts = Counter()
        b_counts = Counter()
        count = 0
        
        for i in range(len(A)):
            a_counts[A[i]] += 1
            b_counts[B[i]] += 1
            
            if A[i] == B[i]:
                if a_counts[A[i]] == b_counts[A[i]]:
                    count += 1
            else:
                if a_counts[A[i]] == b_counts[A[i]]:
                    count += 1

                if a_counts[B[i]] == b_counts[B[i]]:
                    count += 1
                
            
            C.append(count)
            
            
        return C
            