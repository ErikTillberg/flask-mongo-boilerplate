class APIError(Exception):
    """Initialize and APIError."""

    message = ''
    status_code = 400
    code = None

    def __init__(self, *args):
        """Init API Error."""
        Exception.__init__(self, *args)
        if len(args) == 1:
            self.extras = args[0]
        elif len(args) > 1:
            self.extras = args
        else:
            self.extras = None

    def as_dict(self):
        """Create dictionary for the Exception."""
        result = {
            '_cls': self.__class__.__name__,
            'message': self.message,
            'code': self.code
        }
        try:
            print(self.extras)
            result['extras'] = self.extras
        except TypeError:
            result['extras'] = self.__str__()
        return result
