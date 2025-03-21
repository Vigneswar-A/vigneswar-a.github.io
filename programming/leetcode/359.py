class Logger:

    def __init__(self):
        self.time = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.time:
            self.time[message] = timestamp
            return True
        
        if timestamp - self.time[message] >= 10:
            self.time[message] = timestamp
            return True
        
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)