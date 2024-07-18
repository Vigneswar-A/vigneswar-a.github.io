class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        
        
        popularity = Counter()
        for response in responses:
            current_response = Counter()
            for word in response.split():
                if word in features:
                    current_response[word] = 1
            popularity += current_response

        return sorted(features, key=popularity.__getitem__, reverse=1)
                