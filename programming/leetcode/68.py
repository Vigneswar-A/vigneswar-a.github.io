class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i = 0
        res = []
        while i < len(words):
            
            size = 0
            temp = []
            while i < len(words) and size+len(words[i])+1 < maxWidth:
                size += len(words[i])+1
                temp.append(words[i])
                i += 1
                
            if i < len(words) and  size+len(words[i]) <= maxWidth:
                temp.append(words[i])
                size += len(words[i])
                i += 1

            if len(temp) == 1:
                res.append(temp[0]+' '*(maxWidth - len(temp[0])))
                continue       
   
            if i < len(words):
                space = maxWidth - len(''.join(temp))
                evenspace = space//(len(temp)-1)
                extraspace = space%(len(temp)-1)
                line = ''
                for word in temp[:-1]:
                    line += word +  ' '*evenspace
                    if extraspace:
                        line += ' '
                        extraspace -= 1
                res.append(line+temp[-1])
            else:
                space = maxWidth - len(''.join(temp))
                evenspace = space//(len(temp)-1)
                extraspace = space%(len(temp)-1)
                line = ''
                for word in temp[:-1]:
                    line += word +  ' '
                res.append(line+temp[-1]+' '*(maxWidth-len(line+temp[-1])))
            
        return res
            
            