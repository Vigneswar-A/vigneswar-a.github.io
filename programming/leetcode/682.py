class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for operation in ops:
            match operation:
                case '+':
                    record.append(int(record[-1]) + int(record[-2]))
                case 'D':
                    record.append(int(record[-1] * 2))
                case 'C':
                    record.pop()
                case _:
                    record.append(int(operation))
                    
        return sum(record)
                