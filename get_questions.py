import os
import json

with open('programming/solved.json', 'w') as file:
    file.write(json.dumps(os.listdir('programming/leetcode')))
    
