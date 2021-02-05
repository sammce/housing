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
        
    def warn(self, message):
        return self.WARNING + message + self.ENDC

    def fatal(self, message):
        return self.FAIL + message + self.ENDC

    def success(self, message):
        return self.OKGREEN + message + self.ENDC

    def nice(self, message):
        return self.OKCYAN + message + self.ENDC

    def bold(self, message):
        return self.BOLD + message + self.ENDC