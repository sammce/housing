class Formatter():

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
        
    def warn(self, message, end='\n'):
        print(self.WARNING + message + self.ENDC, end=end)

    def fatal(self, message, end='\n'):
        return self.FAIL + message + self.ENDC

    def success(self, message, end='\n'):
        print(self.OKGREEN + message + self.ENDC, end=end)

    def nice(self, message, end='\n'):
        print(self.OKCYAN + message + self.ENDC, end=end)

    def bold(self, message, end='\n'):
        print(self.BOLD + message + self.ENDC, end=end)