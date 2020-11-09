
class IllegalActionError(Exception):

    def __init__(self, action: str, message: str):
        self.action = action
        self.message = message

