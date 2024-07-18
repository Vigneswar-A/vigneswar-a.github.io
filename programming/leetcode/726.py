class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        multipliers = []
        multiplier = 1
        i = len(formula)-1
        counts = Counter()
        
        parsed_formula = []
        i = 0
        while i < len(formula):
            if formula[i] == '(' or formula[i] == ')':
                parsed_formula.append(formula[i])
                i += 1
            elif formula[i].isdigit():
                num = 0
                while i < len(formula) and formula[i].isdigit():
                    num = num*10 + int(formula[i])
                    i += 1
                parsed_formula.append(str(num))
            elif formula[i].isupper():
                atom = formula[i]
                i += 1
                while i < len(formula) and formula[i].islower():
                    atom += formula[i]
                    i += 1
                parsed_formula.append(atom)

        formula = parsed_formula
        i = len(formula)-1
        while i >= 0:
            if formula[i].isdigit() and formula[i-1] != ')':
                counts[formula[i-1]] += int(formula[i]) * multiplier
                i -= 2
            elif formula[i].isdigit() and formula[i-1] == ')':
                multipliers.append(int(formula[i]))
                multiplier *= multipliers[-1]
                i -= 2
            elif formula[i] == '(':
                multiplier //= (multipliers[-1] if multipliers else 1)
                if multipliers:
                    multipliers.pop()
                i -= 1
            elif formula[i] != ')':
                counts[formula[i]] += multiplier
                i -= 1
            else:
                i -= 1
                
        return ''.join(f"{atom}{count if count > 1 else ''}" for atom, count in sorted(counts.items()))
                

                
            