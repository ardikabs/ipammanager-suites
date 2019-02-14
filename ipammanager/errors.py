


class Error(Exception):
    pass

class ServiceUnavailable(Error):
    pass

class NotFound(Error):
    def __init__(self, message):
        self.message = message

class HttpError(Error):
    pass