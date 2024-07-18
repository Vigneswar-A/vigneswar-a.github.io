class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day,month,year = re.fullmatch(r'(\d+)\w+ (\w+) (\d+)', date).groups()
        
        return f"{year}-{months.index(month):0>2}-{day:0>2}"
        
        