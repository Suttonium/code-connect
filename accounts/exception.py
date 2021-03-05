from core.exception import CodeConnectException

class AccountsException(CodeConnectException):
    """
    The AccountsException class is used to distinguish between
    intentionally thrown errors and Django-generated errors.
    """

    ...
