class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)
        rounds = 0
        for i in counts:
            while counts[i]:
                if counts[i] == 1:
                    return -1
                if counts[i] == 2 or counts[i] == 4:
                    counts[i] -= 2
                    rounds += 1
                match counts[i] % 3:
                    case 1:
                        n = (counts[i] // 3) - 1
                        counts[i] -= n * 3
                        rounds += n
                    case (0 | 2 | 3):
                        n = (counts[i] // 3)
                        counts[i] -= n * 3
                        rounds += n
        return rounds
                    
                    