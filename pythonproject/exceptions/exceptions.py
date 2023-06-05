import werkzeug

class InputError(Exception):
    """Exception raised for errors in the input. 

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message: str):
        self.expression = expression
        self.message = message


class LogstringError(InputError):
    """ Raised when the validation of the logstring fails 

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of why the specific transition is not allowed
    """
    def __init__(self, expression, message: str):
        message = "Error in logstring validation! " + message
        super().__init__(expression, message)


class NoFilePartError(werkzeug.exceptions.HTTPException):
    code = 400
    description = 'No file attribute found'


class NoFileSelectedError(werkzeug.exceptions.HTTPException):
    code = 400
    description = 'No selected file'


class UnimplementedFileExtensionError(werkzeug.exceptions.HTTPException):
    code = 500
    description = 'Unimplemented File Extension Error'


class NotAllowedFileExtensionError(werkzeug.exceptions.HTTPException):
    code = 400
    description = 'Not Allowed File Extension Error'








