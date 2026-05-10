class Logger:

    def __init__(self):
        self.logging_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logging_dict and timestamp < self.logging_dict[message]:
            return False
        else:
            self.logging_dict[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
