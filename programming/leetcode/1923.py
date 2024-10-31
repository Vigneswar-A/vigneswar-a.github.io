class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        if sentence1.count(' ') > sentence2.count(' '):
            target = sentence1.split()
            sentence = sentence2.split()
        else:
            target = sentence2.split()
            sentence = sentence1.split()
            
        # add in the beggining case
        for i in range(len(sentence)-1, -1, -1):
            if target[i] != sentence[i]:
                break
        else:
            return True
        
        # add in the ending case
        for i in range(len(sentence)):
            if target[i] != sentence[i]:
                break
        else:
            return True
        
        # add in the middle case
        for i in range(len(sentence)):
            if target[i] != sentence[i]:
                break
        for j in range(i, len(target)):
            k = j
            t = i
            while target[k] == sentence[t]:
                k += 1
                t += 1
                if t == len(sentence) and k == len(target):
                    return True
                elif t == len(sentence) or k == len(target):
                    break
        return False
                
        